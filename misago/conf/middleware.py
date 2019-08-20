


def dynamic_settings_middleware(get_response):
    def middleware(request):
        return get_response(request)
    return middleware