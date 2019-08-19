from django.http import HttpResponse
from django.views import View


class ThreadView(View):
    def get(self):
        return HttpResponse('thread view')