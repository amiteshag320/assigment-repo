from django.core.mail import send_mail
from kids import models as kids_models
from django.conf import settings


def send_email_for_confirmation(email: str, kids_name: str):
    send_mail(
        "Successfull_Attempt",
        "Image of your child {} is been successfully uploaded.".format(kids_name),
        "{}".format(settings.EMAIL_HOST_USER),
        ["{}".format(email)],
        fail_silently=False,
    )
