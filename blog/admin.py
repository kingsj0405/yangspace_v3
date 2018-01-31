from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from reversion.admin import VersionAdmin

from .models import *


@admin.register(Page)
class PageAdmin(MPTTModelAdmin, VersionAdmin):
    mptt_level_indent = 20
