from django.db import models
from django.contrib.auth.models import UserManager as BaseUserManager, PermissionsMixin, AbstractBaseUser


class User(AbstractBaseUser, BaseUserManager):
    ACTIVATION_NONE = 0

    username = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, db_index=True)
    email_hash = models.CharField(max_length=32, unique=True)
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


# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, password, **extra_fields):
#         if not username:
#             raise ValueError("User must have an username.")
#         if not email:
#             raise ValueError("User must have an email address.")

#         # if not extra_fields.get("rank"):
#         #     extra_fields["rank"] = Rank.objects.get_default()

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault("is_superuser", True)
#         return self._create_user(username, email, password, **extra_fields)

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)



