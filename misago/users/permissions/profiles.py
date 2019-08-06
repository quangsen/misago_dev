from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _


def allow_browse_users_list(user_acl):
    if not user_acl['can_browse_users_list']:
        raise PermissionDenied(_("You can't browse users list."))