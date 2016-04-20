# _*_ coding: utf-8
from django.contrib import admin
from .models import Suit
from .models import Branch
from .models import SuitToRent
from .models import SuitToSize
from .models import People
from easy_select2 import select2_modelform
from django.utils import timezone

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
    list_display = ['vendor_code', 'year_issue', 'details', 'colour', 'rent_price', 'item_price', 'note', ]
    list_filter = ['branch']

class SuitToRentAdmin(admin.ModelAdmin):
    form = select2_modelform(SuitToRent)
    fieldsets = [
        (None, {'fields': ['protocol_num']}),
        (u'Информация', {'fields': ['suit_to_size', 'count', 'start_date', 'end_date', 'people', 'total_price', 'is_returned']}),
    ]
    list_display = ('protocol_num', 'suit_to_size', 'people_link', 'start_date', 'end_date', 'item_status_return')
    list_filter = ['published_date']
    search_fields = ['protocol_num']

    ordering = ('is_returned','end_date')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.published_date = timezone.now()
        obj.save()

    readonly_fields = ('people_link', )
    def people_link(self, obj):
        return '<a href="/admin/world/people/%s">%s</a>' \
               % (obj.people.pk, obj.people)
    people_link.allow_tags = True
    people_link.short_description = u"наниматель"

admin.site.register(Suit, SuitAdmin)
admin.site.register(Branch)
admin.site.register(SuitToRent, SuitToRentAdmin)
admin.site.register(People, PeopleAdmin)
