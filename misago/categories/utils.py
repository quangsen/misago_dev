from . import useracl
from .models import Category


def get_categories_tree(request, parent=None, join_posters=False):
    if not request.user_acl['visible_categories']:
        return []

    if parent:
        queryset = parent.get_descendants().order_by('lft')
    else:
        queryset = Category.objects.all_categories()

	flat_list = []
	return flat_list
