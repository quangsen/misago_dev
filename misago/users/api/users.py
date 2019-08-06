from rest_framework import routers, serializers, viewsets
from ..serializers.user import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from ..permissions.profiles import allow_browse_users_list


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        print('gi the ban')
        return HttpResponse('Welcome get_queryset')

    def list(self, request):
        print(request.user_acl)
        # allow_browse_users_list(request.user_acl)
        return HttpResponse('Welcome list')

    def retrieve(self, request, pk=None):
        return HttpResponse('Welcome retrieve')

    def update(self, request, pk=None):
        return HttpResponse('Welcome update')