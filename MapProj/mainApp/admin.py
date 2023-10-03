from django.contrib import admin
from django import forms
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Account)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('account', 'country')
    list_display_links = ('account',)
    list_filter = ('account', 'country')
@admin.register(Impress)
class ImpressyAdmin(admin.ModelAdmin):
    list_display = ('trip', 'date')
    list_filter = ('trip',)
