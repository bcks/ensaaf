from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import *
from image_cropping import ImageCroppingMixin




class ThemeAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Theme
    list_display = ("name",)
    
admin.site.register(Theme, ThemeAdmin)


class VictimAdmin(admin.StackedInline):
    model = Victim
    fields = (
      'video',
      'victim_name',
      'profile_id',
      'gender',
      'age',
      'combatant_status',
      'classification',
      'date_range_start',
      'date_range_end',
      'village',
    )
    extra = 1


class ClipAdmin(ImageCroppingMixin, admin.StackedInline):
    model = Clip
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }
    fields = (
        'video',
        ('start_time_minutes', 'start_time_seconds'),
        ('end_time_minutes', 'end_time_seconds'),
        'theme',
        'transcription'
    )
    extra = 0


class VideoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("title",)
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }
    inlines = [VictimAdmin, ClipAdmin]

admin.site.register(Video, VideoAdmin)



class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "body")
    search_fields = ["title", "body"]

admin.site.register(Page, PageAdmin)
