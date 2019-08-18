from django.shortcuts import render

def categories(request):
	print('vvv', request.user_acl)
	return render(request, 'misago/categories/list.html', {})
