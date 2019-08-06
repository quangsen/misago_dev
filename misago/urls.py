from django.conf.urls import url, include
from misago.core.views import forum_index

app_name = 'misago'

urlpatterns = [
    url(r"^", include('misago.users.urls.api')),
    url(r"^", include("misago.categories.urls")),
    url(r"^", include("misago.threads.urls")),
    url(r"^$", forum_index, name='index'),
]
