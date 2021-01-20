from django.contrib import admin
from .models import Review,Seconday_model
from import_export.admin import ImportExportModelAdmin

admin.site.register(Review)

@admin.register(Seconday_model)
class ViewAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
