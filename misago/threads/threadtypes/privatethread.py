from . import ThreadType
from ...categories import PRIVATE_THREADS_ROOT_NAME
from django.utils.translation import gettext_lazy as _


class PrivateThread(ThreadType):
    root_name = PRIVATE_THREADS_ROOT_NAME

    def get_category_name(self, category):
        return _("Private threads")