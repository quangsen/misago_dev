from .versions import get_cache_versions


def cache_versions_middleware(get_response):
    def middleware(request):
        request.cache_versions = get_cache_versions()
        print('hay', request.cache_versions)
        return get_response(request)

    return middleware