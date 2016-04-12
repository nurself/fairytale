# _*_ coding: utf-8
from django.contrib import admin
from .models import Suit
from .models import Branch
from .models import SuitToRent
from .models import SuitToSize
from .models import People


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


class SuitToRentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['protocol_num']}),
        (u'Информация', {'fields': ['suit_to_size', 'count', 'start_date', 'end_date', 'people', 'total_price']}),
    ]
    search_fields = ['protocol_num']

    def save_model(self, request, obj):
        obj.user = request.user
        obj.save()


admin.site.register(Suit, SuitAdmin)
admin.site.register(Branch)
admin.site.register(SuitToRent, SuitToRentAdmin)
admin.site.register(People)
