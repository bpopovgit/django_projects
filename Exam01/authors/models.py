# authors/models.py
from django.db import models
from .validators import NameValidator, PasscodeValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[NameValidator()]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[NameValidator()]
    )
    passcode = models.CharField(
        max_length=6,
        validators=[PasscodeValidator()],
        help_text="Your passcode must be a combination of 6 digits"
    )
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
