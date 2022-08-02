from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cars, Callback, CarsShots


class CarsShotsInline(admin.TabularInline):
    model = CarsShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    inlines = [CarsShotsInline]


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    pass
