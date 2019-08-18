from misago.core.views import home_redirect
from django.conf.urls import url
from ..views import categories


urlpatterns = [
    url(r"^categories/$", categories, name='categories')
]
