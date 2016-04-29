# _*_ coding: utf-8
from django.contrib import admin
from .models import Suit
from .models import Branch
from .models import SuitToRent
from .models import SuitToSize
from .models import People
from .models import SuitType
from .models import Agreement
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
        total = Agreement()
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

class SuitListFilter(admin.SimpleListFilter):
    title = (u"Филиалы")

    parameter_name = 'branch'

    def lookups(self, request, model_admin):
        branches = Branch.objects.all();
        if request.user.is_admin:
            return (
                (branch.pk,branch.name) for branch in branches
                )
        else:
            return (
            (request.user.branch.pk, (request.user.branch.name)),
            )

    def queryset(self, request, queryset):
        if request.user.is_admin:
            if not self.value():
                return Suit.objects.all()
            else:
                return Suit.objects.filter(branch=self.value())
        else:
            return Suit.objects.filter(branch=request.user.branch)


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
    list_filter = [SuitListFilter,'type',]
    list_per_page = 10

    def render_change_form(self, request, context, *args, **kwargs):
        if request.user.is_admin:
            context['adminform'].form.fields['branch'].queryset = Branch.objects.all()
        else:
            context['adminform'].form.fields['branch'].queryset = Branch.objects.filter(pk=request.user.branch.pk)
        return super(SuitAdmin, self).render_change_form(request, context, args, kwargs)


class AgreementListFilter(admin.SimpleListFilter):
    title = (u"Пользователи")

    parameter_name = 'authorization'

    def lookups(self, request, model_admin):
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
                return Agreement.objects.all()
            else:
                return Agreement.objects.filter(user=self.value())
        else:
            return Agreement.objects.filter(user=request.user)


class SuitToRentInline(admin.StackedInline):
    model = SuitToRent
    form = select2_modelform(SuitToRent)
    fieldsets = [
        ( None, {'fields': ['suit_to_size', 'count',]}),
    ]
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs["queryset"] = SuitToSize.objects.filter(suit__branch=request.user.branch)
        return super(SuitToRentInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class AgreementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['protocol_num']}),
        (u'Информация', {'fields': ['start_date', 'end_date', 'people', 'reserve_sum', 'total_price', 'is_returned']}),
    ]
    inlines = [SuitToRentInline]
    search_fields = ['protocol_num']
    ordering = ('is_returned','end_date')
    readonly_fields = ('people_link', )
    list_filter = (AgreementListFilter, 'start_date')

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

    list_display = ('protocol_num', 'people_link', 'start_date', 'end_date', 'reserve_sum', 'total_price', 'item_status_return')
    list_per_page = 5


class UserCreationForm(forms.ModelForm):
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
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'branch', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'branch', 'is_admin', 'is_active', 'is_staff')
    list_filter = ('branch',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('branch',)}),
        ('Permissions', {'fields': ('is_admin','is_active',)}),
    )
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
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.unregister(Group)
