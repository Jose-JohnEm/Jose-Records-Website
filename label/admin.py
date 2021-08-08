from django.contrib import admin
from django.utils.html import mark_safe

# Register your models here.
from .models import *

@admin.register(ArtistLabel)
class ArtistLabelPageAdmin(admin.ModelAdmin):
    fieldsets = [[
        None, {
            'fields': ('name', 'labeled', 'picture', 'text')
        }
    ]]

    def selected_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.picture.url,
            width=obj.picture.width,
            height=obj.picture.height)
        )

@admin.register(ProdType)
class ProdTypePageAdmin(admin.ModelAdmin):
    fieldsets = [[
        None, {
            'fields': ['name']
        }
    ]]

@admin.register(Prodbeat)
class ProdBeatPageAdmin(admin.ModelAdmin):
    fieldsets = [[
        None, {
            'fields': ['name', 'reference', 'music', 'genre']
        }
    ]]