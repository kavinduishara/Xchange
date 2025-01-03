from django.contrib import admin

# Register your models here.
from .models import Listing,LikedList

class ListingAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

class LikedListAdmin(admin.ModelAdmin):
    readonly_fields=('id',)

admin.site.register(Listing,ListingAdmin)
admin.site.register(LikedList,LikedListAdmin)