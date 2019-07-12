from django.conf.urls import url, include
from ..api import auth
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from ..api import mention


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        print('gi the ban')
        return HttpResponse('Welcome get_queryset')

    def list(self, request):
        return HttpResponse('Welcome list')

    def retrieve(self, request, pk=None):
        return HttpResponse('Welcome retrieve')

    def update(self, request, pk=None):
        return HttpResponse('Welcome update')


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^auth/$', auth.gateway, name='auth'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r"^mention/$", mention.mention_suggestions, name='mention-suggestions')
]
