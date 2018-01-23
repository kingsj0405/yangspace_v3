from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class PageMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Page, PageMPTTModelAdmin)
