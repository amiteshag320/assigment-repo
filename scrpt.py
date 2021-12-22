import django
from django.templatetags.static import static
from django.conf import settings

django.setup()

from kids import models as kids_models

import os


kids_name_list = ["Amitesh", "Aditya", "Adarsh", "Piyush", "Mihir"]
kids_age_list = [10, 12, 14, 14, 12]
kids_parent_num_list = [
    +91923456789,
    +91923456788,
    +91923456787,
    +91923456786,
    +91923456785,
]
kids_parent_email = [
    "amitesh@gmail.com",
    "aditya@gmail.com",
    "adarsh@gmail.com",
    "piyush@gmail.com",
    "mihir@gmail.com",
]


def func():
    for i in range(5):
        kids = kids_models.Kid()
        kids.kid_name = kids_name_list[i]
        kids.kid_age = kids_age_list[i]
        kids.parent_num = kids_parent_num_list[i]
        kids.parent_email = kids_parent_email[i]
        kids.save()


def add_image():

    image = kids_models.Image()
    main_kid = kids_models.Kid.objects.get(pk=1)
    image.kid = main_kid
    image.actual_image = static("images/fruit.jpeg")
    image.is_approved = True
    image.approved_by = "Amit"
    image.food_group = "F"
    image.save()


if __name__ == "__main__":
    func()
