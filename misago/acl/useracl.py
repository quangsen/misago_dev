import copy
from . import buildacl
from .cache import get_acl_cache, set_acl_cache


def get_user_acl(user, cache_versions):
	user_acl = get_acl_cache(user, cache_versions)
	if user_acl is None:
		user_acl = buildacl.build_acl(user.get_roles())
		set_acl_cache(user, cache_versions, user_acl)
	user_acl['user_id'] = user.user_id
	user_acl['is_authenticated'] = bool(user.is_authenticated)
	user_acl['is_anonymous'] = bool(user.is_anonymous)
	user_acl['is_staff'] = user.is_staff
	user_acl['is_superuser'] = user.is_superuser
	user_acl['cache_versions'] = cache_versions.copy()
	return user_acl