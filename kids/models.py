from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.dispatch import receiver
from phone_field import PhoneField
from django.utils.html import format_html, mark_safe
from django.db.models.signals import post_save
from kids import helper


class Kid(models.Model):
    kid_name = models.CharField(max_length=100, blank=False, null=False)
    kid_age = models.IntegerField(blank=False, null=False)
    parent_num = PhoneField(blank=False, null=False)
    parent_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):

    FOOD_CHOICE = [
        ("F", "Fruit"),
        ("V", "Vegetable"),
        ("G", "Grain"),
        ("P", "Protein"),
        ("D", "Dairy"),
    ]

    kid = models.ForeignKey(Kid, blank=True, null=True, on_delete=models.SET_NULL)
    actual_image = ImageField(upload_to="images/", null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    food_group = models.CharField(
        max_length=1, choices=FOOD_CHOICE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_url(self):
        return self.actual_image.url

    def show_image(self):
        return format_html(
            '<img src="{}" width="500" height="500" />'.format(self.actual_image.url)
        )


@receiver(post_save, sender=Image)
def trigger_fun(sender, instance, created, **kwargs):
    if created:
        kids_obj = instance.kid
        name = kids_obj.kid_name
        email = kids_obj.parent_email
        helper.send_email_for_confirmation(email, name)


# Create your models here.
