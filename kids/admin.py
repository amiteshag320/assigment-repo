from django.contrib import admin
from kids import models as kids_models


class KidAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "kid_name",
        "kid_age",
        "parent_num",
        "parent_email",
        "created_at",
        "updated_at",
    ]


class ImageAdmin(admin.ModelAdmin):

    list_display = [
        "kid",
        "actual_image",
        "image_url",
        "is_approved",
        "food_group",
        "updated_at",
        "created_at",
    ]
    readonly_fields = ["image_url", "show_image"]


# Register your models here.
admin.site.register(kids_models.Kid, KidAdmin)
admin.site.register(kids_models.Image, ImageAdmin)
