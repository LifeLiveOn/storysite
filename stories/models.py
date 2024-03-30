from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class Story(models.Model):
    story_name = models.CharField(max_length=255)
    story_description = models.TextField(max_length=500)
    story_image = models.ImageField(upload_to='storyImages/')
    is_valid = models.BooleanField(default=False)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    storyID = models.OneToOneField("Story", on_delete=models.CASCADE, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, blank=True)
    last_login = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.__get_short_name()

    def __get_full_name(self):
        return self.name

    def __get_short_name(self):
        return self.email.split('@')[0]


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='eventImages/')
    date = models.DateField()
    story = models.ForeignKey("Story", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]
