from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, RedirectView

from library_app.forms import LoginForm
from library_app.models import Book


class LoginView(FormView):
    template_name = 'ui/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')


class DashboardView(LoginRequiredMixin, ListView):
    model = Book
    login_url = 'login/'
    template_name = 'ui/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['lol'] = 'max'
        return context
