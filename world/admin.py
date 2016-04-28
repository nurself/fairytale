# _*_ coding: utf-8
from django.contrib import admin
from .models import Suit
from .models import Branch
from .models import SuitToRent
from .models import SuitToSize
from .models import People
from .models import SuitType
from easy_select2 import select2_modelform
from django.utils import timezone
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum
from .models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from django.forms.models import  ModelForm

class TotalChangeList(ChangeList):
    fields_to_total = ['total_price','reserve_sum']

    def get_total_values(self, queryset):
        total = SuitToRent()
        total.protocol_num = u"Итого"
        total.start_date = timezone.now().date()
        total.end_date = timezone.now().date()

        for field in self.fields_to_total:
            setattr(total, field, queryset.aggregate(Sum(field))[field + '__sum'])
        return total

    def get_results(self, request):
        super(TotalChangeList, self).get_results(request)
        total = self.get_total_values(self.queryset)
        len(self.result_list)
        self.result_list._result_cache.append(total)


class PeopleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'passport_data', 'address', 'phone']}),
    ]
    list_display = ['name', 'passport_data', 'address', 'phone', ]
    search_fields = ['name']

class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        return True

class SuitToSizeInline(admin.StackedInline):
    model = SuitToSize
    fieldsets = [
        (None, {'fields': ['size', 'count']}),
    ]
    extra = 1
    form = AlwaysChangedModelForm


class SuitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type']}),
        (u'Информация', {
            'fields': ['picture', 'vendor_code', 'year_issue', 'details', 'colour', 'rent_price', 'item_price', 'note',
                       'branch']}),
    ]
    inlines = [SuitToSizeInline]
    search_fields = ['name']
    list_display = ['name', 'vendor_code', 'admin_image', 'year_issue', 'details', 'colour', 'rent_price', 'item_price', 'note', ]
    list_filter = ['branch','type',]
    list_per_page = 10

class SuitToRentListFilter(admin.SimpleListFilter):
    title = (u"Пользователи")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'authorization'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        users = MyUser.objects.all();
        if request.user.is_admin:
            return (
                (user.pk,user.email) for user in users
                )
        else:
            return (
            (request.user, (request.user)),
            )

    def queryset(self, request, queryset):
        if request.user.is_admin:
            if not self.value():
                return SuitToRent.objects.all()
            else:
                return SuitToRent.objects.filter(user=self.value())
        else:
            return SuitToRent.objects.filter(user=request.user)

class SuitToRentAdmin(admin.ModelAdmin):
    form = select2_modelform(SuitToRent)
    fieldsets = [
        (None, {'fields': ['protocol_num']}),
        (u'Информация', {'fields': ['suit_to_size', 'count', 'start_date', 'end_date', 'people', 'reserve_sum', 'total_price', 'is_returned']}),
    ]
    list_filter = (SuitToRentListFilter,)
    search_fields = ['protocol_num']
    ordering = ('is_returned','end_date')
    readonly_fields = ('people_link', )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.published_date = timezone.now()
        obj.save()

    def people_link(self, obj):
        return '<a href="/admin/world/people/%s">%s</a>' \
               % (obj.people.pk, obj.people)
    people_link.allow_tags = True
    people_link.short_description = u"наниматель"

    def get_changelist(self, request, **kwargs):
        """Override the default changelist"""
        return TotalChangeList

    list_display = ('protocol_num', 'suit_to_size', 'people_link', 'start_date', 'end_date', 'reserve_sum', 'total_price', 'item_status_return')
    list_per_page = 5

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'branch')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'branch', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'branch', 'is_admin', 'is_active', 'is_staff')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('branch',)}),
        ('Permissions', {'fields': ('is_admin','is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'branch', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def has_delete_permission(self, request, obj=None):
        return request.user.is_admin

    def has_add_permission(self, request):
        return request.user.is_admin

    def has_change_permission(self, request, obj=None):
        return request.user.is_admin


admin.site.register(MyUser, UserAdmin)
admin.site.register(Suit, SuitAdmin)
admin.site.register(Branch)
admin.site.register(SuitType)
admin.site.register(SuitToRent, SuitToRentAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.unregister(Group)
