from django.contrib import admin
from .models import Footwear
from .models import Top
from .models import Bottom
from .models import Accessorie


class FootwearAdmin(admin.ModelAdmin):
    list_display = ("name", "tags")


class TopAdmin(admin.ModelAdmin):
    list_display = ("name", "tags")


class BottomAdmin(admin.ModelAdmin):
    list_display = ("name", "tags")


class AccessorieAdmin(admin.ModelAdmin):
    list_display = ("name", "tags")


admin.site.register(Footwear, FootwearAdmin)
admin.site.register(Top, TopAdmin)
admin.site.register(Bottom, BottomAdmin)
admin.site.register(Accessorie, AccessorieAdmin)