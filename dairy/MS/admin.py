from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(StaffInfo)

class CowInfoAdmin(admin.ModelAdmin):
    list_display = ('cow_control_number', 'gender', 'cow_type', 'date_of_birth', 'animal_status')
admin.site.register(CowInfo,CowInfoAdmin)

class VaccineMonitoringAdmin(admin.ModelAdmin):
    list_display = ('cow_number', 'date', 'remarks')
admin.site.register(VaccineMonitoring,VaccineMonitoringAdmin)

class FeedMonitoringAdmin(admin.ModelAdmin):
    list_display = ('cow_number', 'date', 'remarks', 'food_item', 'quantity', 'feeding_time')
admin.site.register(FeedMonitoring,FeedMonitoringAdmin)

class MilkCollectionAdmin(admin.ModelAdmin):
    list_display = ('collection_id', 'cow_number', 'date', 'liter', 'price_per_liter', 'total')
admin.site.register(MilkCollection,MilkCollectionAdmin)

class MilkSaleAdmin(admin.ModelAdmin):
    list_display = ('collection_number', 'customer_name', 'liter', 'price_per_liter', 'total', 'date')
admin.site.register(MilkSale,MilkSaleAdmin)

class MilkSaleReportAdmin(admin.ModelAdmin):
    list_display = ('cow_number', 'liter', 'price_per_liter', 'total', 'date')
admin.site.register(MilkSaleReport,MilkSaleReportAdmin)

class CowSaleAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'date', 'cow_number', 'amount', 'customer_name', 'customer_contact', 'customer_email', 'remarks')
admin.site.register(CowSale,CowSaleAdmin)

class CowSaleReportAdmin(admin.ModelAdmin):
    list_display = ('cow_number', 'date', 'amount')
admin.site.register(CowSaleReport,CowSaleReportAdmin)