from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class MyUser(EmailAbstractUser):
    # Custom fields
    # email = EmailField(verbose_name="email", max_length=70, unique=True)
    # date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)

    # Required
    objects = EmailUserManager()
