from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    """ User
    """

    class Gender(models.TextChoices):
        MALE = 'M', _('male')
        FEMALE = 'F', _('female')

    nickname = models.CharField(max_length=30, null=False, blank=False)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.MALE,
    )

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "User"
