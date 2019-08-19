from django.shortcuts import render

def categories(request):
	print('vvv-quang', request.user.acl_key)
	return render(request, 'misago/categories/list.html', {})
