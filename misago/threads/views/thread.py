from django.http import HttpResponse
from django.views import View


class ThreadView(View):
    print('det')
    def get(self):
        print('lili')
        return HttpResponse('thread view')