from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import UserManager as AbastractUserManager, AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

phone_regex_validator = RegexValidator(
    regex=r"^\+?1?\d{9,12}$",
    message=_("Номер телефона необходимо вводить в формате: «+99891234567». Допускается до 13 цифр."),
)


class UserManager(AbastractUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(
        verbose_name=_("Phone number"),
        max_length=16,
        unique=True,
        validators=(phone_regex_validator,),
    )
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
    first_name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='user')
    """
    password_set:
        We set this to False when user is registered with social auth.  Because we don't get password in social auth.
        we send this in user details to frontend. So that frontend shows "set password" button instead of "change
        password" set to True when user sets password
    """
    password_set = models.BooleanField(default=True, editable=False)

    password_changed_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        if self.phone_number:
            user = User.objects.filter(phone_number=self.phone_number).first()
            if user and user.id != self.id:
                raise ValidationError(_("User with this phone number already exists."))
        super().save(*args, **kwargs)

    @staticmethod
    def is_validate_password(password) -> bool:
        """Validate password"""
        if not password:
            return False
        if len(password) < 5:
            return False
        if len(password) > 20:
            return False
        if " " in password:
            return False
        if not password.isascii():
            return False
        return True


