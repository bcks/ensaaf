from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import *
from image_cropping import ImageCroppingMixin




class ThemeAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Theme
    list_display = ("name",)

admin.site.register(Theme, ThemeAdmin)


class ClipAdmin(admin.StackedInline):
    model = Clip
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }
    extra = 0


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ClipAdmin]

admin.site.register(Video, VideoAdmin)


class ClipAloneAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

admin.site.register(Clip, ClipAloneAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "body")
    search_fields = ["title", "body"]

admin.site.register(Page, PageAdmin)
