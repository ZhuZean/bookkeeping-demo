from django.contrib import admin
from api.models import Payment, Usage, Currency, Bill

# manage models on the admin site
class PaymentAdmin(admin.ModelAdmin):
    list_display=['name', 'created_at', 'updated_at']


class UsageAdmin(admin.ModelAdmin):
    list_display=['name', 'created_at', 'updated_at']


class CurrencyAdmin(admin.ModelAdmin):
    list_display=['name', 'created_at', 'updated_at']


class BillAdmin(admin.ModelAdmin):
    list_display=['payment', 'bill_type', 'usage', 'currency', 'price', 'note', 'created_at', 'updated_at']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        formfield = super().formfield_for_manytomany(db_field, request, **kwargs)
        # For example, we can add the instance id to the original string
        formfield.label_from_instance = lambda instance: '{} (id={})'.format(instance, instance.id)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Usage, UsageAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Bill, BillAdmin)
