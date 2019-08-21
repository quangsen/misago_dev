from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey
from ..threads.threadtypes import trees_map
from . import PRIVATE_THREADS_ROOT_NAME, THREADS_ROOT_NAME
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryManager(TreeManager):
    def all_categories(self, include_root=False):
        tree_id = trees_map.get_tree_id_for_root(THREADS_ROOT_NAME)
        queryset = self.filter(tree_id=tree_id)
        if not include_root:
            queryset = queryset.filter(level__gt=0)
        return queryset.order_by('lft')


class Category(MPTTModel):
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    special_role = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    threads = models.PositiveIntegerField(default=0)
    posts = models.PositiveIntegerField(default=0)
    last_post_on = models.DateTimeField(null=True, blank=True)
    last_thread_title = models.CharField(max_length=255, null=True, blank=True)
    last_thread_slug = models.CharField(max_length=255, null=True, blank=True)
    last_poster_name = models.CharField(max_length=255, null=True, blank=True)
    last_poster_slug = models.CharField(max_length=255, null=True, blank=True)
    require_threads_approval = models.BooleanField(default=False)
    require_replies_approval = models.BooleanField(default=False)
    require_edits_approval = models.BooleanField(default=False)
    prune_started_after = models.PositiveIntegerField(default=0)
    prune_replied_after = models.PositiveIntegerField(default=0)
    css_class = models.CharField(max_length=255, null=True, blank=True)
    last_poster = models.ForeignKey(User, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    
    objects = CategoryManager()
    
    def __str__(self):
        return self.name


