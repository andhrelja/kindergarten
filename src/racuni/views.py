from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm


class LoginView(LoginView):
    form_class = LoginForm
