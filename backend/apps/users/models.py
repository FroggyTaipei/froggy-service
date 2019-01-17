from uuid import uuid4

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(email=self.normalize_email(email),
                          is_active=True,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=timezone.now(),
                          registered_at=timezone.now(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(email, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)

    def create_accountkit_user(self, **extra_fields):
        email = extra_fields.pop('email', None)
        mobile = extra_fields.pop('mobile', None)
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        if is_staff or is_superuser:
            raise ValidationError('Cannot set accountkit user to staff or superuser.')
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email,
                          mobile=mobile,
                          is_active=True,
                          is_staff=False,
                          is_superuser=False,
                          last_login=timezone.now(),
                          registered_at=timezone.now(),
                          **extra_fields)
        user.set_password(BaseUserManager().make_random_password())
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email'), unique=True, null=True, max_length=255)
    mobile = PhoneNumberField(verbose_name=_('Mobile'), unique=True, null=True)

    full_name = models.CharField(verbose_name=_('Full Name'), max_length=30, default=_('Unknown User'))
    avatar = models.ImageField(verbose_name=_('Avatar Setting'), blank=True)
    token = models.UUIDField(verbose_name='Token', default=uuid4, editable=False)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)
    registered_at = models.DateTimeField(verbose_name=_('Registered At'), auto_now_add=timezone.now)

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.full_name

    @property
    def first_name(self):
        return self.full_name

    def avatar_tag(self):
        if self.avatar:
            return mark_safe(f'<img src="{self.avatar.url}" width="150"/>')
        return ''
    avatar_tag.short_description = _('Avatar')

    def clean(self, *args, **kwargs):
        if not self.email and not self.mobile:
            raise ValidationError('Must provide email or mobile.')
        return super(User, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        return super(User, self).save(*args, **kwargs)
