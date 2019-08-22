from django.shortcuts import render
from .utils import get_categories_tree
from django.core.mail import send_mail
from django.conf import settings


def categories(request):
	# print('toan', request.user_acl)
	send_mail(
		'Subject here',
		'Here is the message.',
		settings.EMAIL_HOST_USER,
		['quangsen283@gmail.com'],
		# fail_silently=False,
	)
	# categories_tree = get_categories_tree(request, join_posters=True)
	return render(request, 'misago/categories/list.html', {})
