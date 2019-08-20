from . import useracl


def user_acl_middleware(get_response):
	def middleware(request):
		request.user_acl = useracl.get_user_acl(request.user, request.cache_versions)
		return get_response(request)
		
	return middleware