from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        pass

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser):
    ACTIVATION_NONE = 0

    username = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, db_index=True)
    email = models.EmailField(max_length=255, db_index=True, unique=True)
    email_hash = models.CharField(max_length=32)
    title = models.CharField(max_length=255, null=True, blank=True)
    requires_activation = models.PositiveIntegerField(default=ACTIVATION_NONE)
    acl_key = models.CharField(max_length=12, null=True, blank=True)
    is_active_staff_message = models.TextField(null=True, blank=True)
    is_deleting_account = models.BooleanField(default=False)
    avatar_crop = models.CharField(max_length=255, null=True, blank=True)
    is_avatar_locked = models.BooleanField(default=False)
    avatar_lock_user_message = models.TextField(null=True, blank=True)
    avatar_lock_staff_message = models.TextField(null=True, blank=True)
    signature = models.TextField(null=True, blank=True)
    signature_parsed = models.TextField(null=True, blank=True)
    signature_checksum = models.CharField(max_length=64, null=True, blank=True)
    is_signature_locked = models.BooleanField(default=False)
    signature_lock_user_message = models.TextField(null=True, blank=True)
    signature_lock_staff_message = models.TextField(null=True, blank=True)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    unread_private_threads = models.PositiveIntegerField(default=0)
    sync_unread_private_threads = models.BooleanField(default=False)
    threads = models.PositiveIntegerField(default=0)
    posts = models.PositiveIntegerField(default=0, db_index=True)
    last_posted_on = models.DateTimeField(null=True, blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into admin sites."),
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()