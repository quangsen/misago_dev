from django.conf.urls import url
from misago.threads.views.thread import ThreadView
from misago.conf import settings
from misago.threads.views.list import ForumThreadsList, CategoryThreadsList, PrivateThreadsList

LISTS_TYPES = ("all", "my", "new", "unread", "subscribed", "unapproved")


def threads_list_patterns(prefix, view, patterns):
    urls = []
    for i, pattern in enumerate(patterns):
        if i > 0:
            url_name = "%s-%s" % (prefix, LISTS_TYPES[i])
        else:
            url_name = prefix

        urls.append(
            url(
                pattern,
                view.as_view(),
                name=url_name,
                kwargs={"list_type": LISTS_TYPES[i]},
            )
        )
    return urls


if settings.MISAGO_THREADS_ON_INDEX:
    urlpatterns = threads_list_patterns(
        "threads",
        ForumThreadsList,
        (r"^$", r"^my/$", r"^new/$", r"^unread/$", r"^subscribed/$", r"^unapproved/$"),
    )
else:
    urlpatterns = threads_list_patterns(
        "threads",
        ForumThreadsList,
        (
            r"^threads/$",
            r"^threads/my/$",
            r"^threads/new/$",
            r"^threads/unread/$",
            r"^threads/subscribed/$",
            r"^threads/unapproved/$",
        ),
    )
    
print('vvvdd', urlpatterns)
# else:
#     urlpatterns = threads_list_patterns(
#         "threads",
#         ForumThreadsList,
#         (
#             r"^threads/$",
#             r"^threads/my/$",
#             r"^threads/new/$",
#             r"^threads/unread/$",
#             r"^threads/subscribed/$",
#             r"^threads/unapproved/$",
#         ),
#     )


# urlpatterns += threads_list_patterns(
#     "category",
#     CategoryThreadsList,
#     (
#         r"^c/(?P<slug>[-a-zA-Z0-9]+)/(?P<pk>\d+)/$",
#         r"^c/(?P<slug>[-a-zA-Z0-9]+)/(?P<pk>\d+)/my/$",
#         r"^c/(?P<slug>[-a-zA-Z0-9]+)/(?P<pk>\d+)/new/$",
#         r"^c/(?P<slug>[-a-zA-Z0-9]+)/(?P<pk>\d+)/unread/$",
#         r"^c/(?P<slug>[-a-zA-Z0-9]+)/(?P<pk>\d+)/subscribed/$",
#         r"^c/(?P<slug>[-a-zA-Z0-9]+)/(?P<pk>\d+)/unapproved/$",
#     ),
# )

# urlpatterns += threads_list_patterns(
#     "private-threads",
#     PrivateThreadsList,
#     (
#         r"^private-threads/$",
#         r"^private-threads/my/$",
#         r"^private-threads/new/$",
#         r"^private-threads/unread/$",
#         r"^private-threads/subscribed/$",
#     ),
# )