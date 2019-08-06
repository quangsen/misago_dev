from misago.core.views import home_redirect
from django.conf.urls import url


urlpatterns = [
    url(r"^categories/$", home_redirect)
]
