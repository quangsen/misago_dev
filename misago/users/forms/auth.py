from django.utils.translation import gettext_lazy as _
from django import forms
# from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm

class MisagoAuthMixin:
    error_messages = {
        "empty_data": _("Fill out both fields."),
        "invalid_login": _("Login or password is incorrect."),
        "inactive_user": _(
            "You have to activate your account before you will be able to sign in."
        ),
        "inactive_admin": _(
            "Your account has to be activated by site administrator "
            "before you will be able to sign in."
        ),
    }

    def confirm_user_active(self, user):
        apass

    def confirm_user_not_banned(self, user):
        pass

    def get_errors_dict(self):
        pass

class AuthenticationForm():
    username = forms.CharField(
        label=_("Username or e-mail"), max_length=254, required=False
    )
    password = forms.CharField(
        label=_("Password"), strip=False, required=False, widget=forms.PasswordInput
    )

    def clean(self):
        print('gi eo hieu')
        pass

    def confirm_login_allowed(self, user):
        pass
