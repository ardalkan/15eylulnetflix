from django.contrib import admin
from .models import *
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('olusturan','isim','slug')
    list_display_links = ( 'olusturan',)
    search_fields = ('isim',)
    list_filter =('olusturan',)
    list_per_page = 1
    # list_editable = ('isim',)
    readonly_fields = ('slug','id')

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Hesap)