from django.shortcuts import render

def categories(request):
	print('vvv-quang', request.user.is_staff)
	return render(request, 'misago/categories/list.html', {})
