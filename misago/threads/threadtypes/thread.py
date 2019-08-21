from . import ThreadType
from ...categories import THREADS_ROOT_NAME
from django.utils.translation import gettext_lazy as _


class Thread(ThreadType):
    root_name = THREADS_ROOT_NAME

    def get_category_name(self, category):
        if category.level:
            return category.name
        return _("None (will become top level category)")