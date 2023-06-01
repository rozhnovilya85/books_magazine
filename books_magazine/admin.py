from django.contrib import admin
from metatags.admin import MetaTagInline


class CustomModelAdmin(admin.ModelAdmin):
    inlines = (MetaTagInline,)