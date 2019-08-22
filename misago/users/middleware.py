from django.utils.deprecation import MiddlewareMixin
from .models import AnonymousUser
from .bans import get_request_ip_ban, get_user_ban
from django.contrib.auth import logout


class RealIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            request.user_ip = x_forwarded_for.split(',')[0]
        else:
            request.user_ip = request.META.get('REMOTE_ADDR')


class UserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_anonymous:
            request.user = AnonymousUser()