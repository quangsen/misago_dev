from django.views import View
from django.http import HttpResponse


class ThreadsList(View):
    def get(self, request):
        print('get')
        return HttpResponse('get')

    def get_category(self, request):
        print('get')
        return HttpResponse('get_category')

    def get_threads(self, request):
        print('get')
        return HttpResponse('get_threads')

    def get_frontend_context(self, request):
        print('get')
        return HttpResponse('get_threads')


class ForumThreadsList(ThreadsList):
    pass


class CategoryThreadsList(ForumThreadsList):
    pass


class PrivateThreadsList(ThreadsList):
    pass