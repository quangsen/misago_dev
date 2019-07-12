from ..forms.auth import AuthenticationForm

def gateway(request):
    if request.method == 'POST':
        return login(request)


def login(request):
    form = AuthenticationForm(request, data=request.data)
    if form.is_valid():
        auth.login(request, form.user_cache)

