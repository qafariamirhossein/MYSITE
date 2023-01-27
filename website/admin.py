from django.contrib import admin
from website.models import  Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','email','created_date')


admin.site.register(Contact,ContactAdmin)