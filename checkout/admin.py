from django.contrib import admin
from .models import CheckOut
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CheckoutAdminview(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['first_name','last_name','address','Payment_status','checkout_date']
    list_filter = ['username','Payment_status','checkout_date']

admin.site.register(CheckOut,CheckoutAdminview)
