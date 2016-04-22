# _*_ coding: utf-8
from django.contrib import admin
from .models import Suit
from .models import Branch
from .models import SuitToRent
from .models import SuitToSize
from .models import People
from easy_select2 import select2_modelform
from django.utils import timezone
from django.contrib.admin.views.main import ChangeList
from django.db.models import Avg, Sum


class TotalChangeList(ChangeList):
    fields_to_total = ['total_price',]

    def get_total_values(self, queryset):
        total = SuitToRent()
        total.protocol_num = u"Итого"
        total.start_date = timezone.now().date()
        total.end_date = timezone.now().date()

        for field in self.fields_to_total:
            setattr(total, field, queryset.aggregate(Sum(field))['total_price__sum'])
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

class SuitToSizeInline(admin.StackedInline):
    model = SuitToSize
    fieldsets = [
        (None, {'fields': ['size', 'count']}),
    ]
    extra = 1


class SuitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (u'Информация', {
            'fields': ['picture', 'vendor_code', 'year_issue', 'details', 'colour', 'rent_price', 'item_price', 'note',
                       'branch']}),
    ]
    inlines = [SuitToSizeInline]
    search_fields = ['name']
    list_display = ['name', 'vendor_code', 'year_issue', 'details', 'colour', 'rent_price', 'item_price', 'note', ]
    list_filter = ['branch']

class SuitToRentAdmin(admin.ModelAdmin):
    form = select2_modelform(SuitToRent)
    fieldsets = [
        (None, {'fields': ['protocol_num']}),
        (u'Информация', {'fields': ['suit_to_size', 'count', 'start_date', 'end_date', 'people', 'total_price', 'is_returned']}),
    ]
    list_filter = ['published_date']
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

    list_display = ('protocol_num', 'suit_to_size', 'people_link', 'start_date', 'end_date', 'total_price', 'item_status_return')

admin.site.register(Suit, SuitAdmin)
admin.site.register(Branch)
admin.site.register(SuitToRent, SuitToRentAdmin)
admin.site.register(People, PeopleAdmin)