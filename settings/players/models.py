from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='email address')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    is_database_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


GENDER = [('FEMALE', 'FEMALE'), ('MALE', 'MALE')]


class ChessPlayers(models.Model):
    fide_id = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name_fide = models.CharField(max_length=20)
    first_name_fide = models.CharField(max_length=20)
    title = models.CharField(max_length=2)
    gender = models.CharField(choices=GENDER, max_length=14)
    federation = models.CharField(max_length=3)
    rating_classical = models.CharField(max_length=4)
    rating_rapid = models.CharField(max_length=4)
    rating_blitz = models.CharField(max_length=4)
    region = models.ForeignKey('Region', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
class Region(models.Model):
    title = models.CharField('Название', max_length=40)

    def __str__(self):
        return self.title

