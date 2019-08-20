from .models import CacheVersion
from django.core.cache import cache


CACHE_NAME = "cache_versions"


def get_cache_versions():
    cache_versions = get_cache_versions_from_cache()
    if cache_versions is None:
        cache_versions = get_cache_versions_from_db()
        cache.set(CACHE_NAME, cache_versions)
    return cache_versions


def get_cache_versions_from_cache():
    return cache.get(CACHE_NAME)


def get_cache_versions_from_db():
    queryset = CacheVersion.objects.all()
    return {i.cache: i.version for i in queryset}