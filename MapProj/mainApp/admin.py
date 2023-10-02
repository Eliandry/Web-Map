from django.contrib import admin
from django import forms
from .models import *

@admin.register(Country)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Account)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Trip)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'country')
    list_display_links = ('account',)
    list_filter = ('account', 'country')
@admin.register(Impress)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('trip', 'date')
    list_filter = ('trip',)
