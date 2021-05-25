from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import *




class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    list_display = ('name', )


class ClipAdmin(admin.StackedInline):
    model = Clip
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    extra = 0


class VideoAdmin(admin.ModelAdmin):
     list_display = ('title', )
     inlines = [ClipAdmin]
 
admin.site.register(Video, VideoAdmin)


admin.site.register(Clip)
admin.site.register(Theme, ThemeAdmin)
