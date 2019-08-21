from django.shortcuts import render
from .utils import get_categories_tree


def categories(request):
	print('toan', request.user)
	# categories_tree = get_categories_tree(request, join_posters=True)
	return render(request, 'misago/categories/list.html', {})
