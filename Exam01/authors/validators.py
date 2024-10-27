# authors/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __call__(self, value):
        if not re.match("^[a-zA-Z]+$", value):
            raise ValidationError("Your name must contain letters only!")


@deconstructible
class PasscodeValidator:
    def __call__(self, value):
        if not re.match("^\d{6}$", value):
            raise ValidationError("Your passcode must be exactly 6 digits!")
