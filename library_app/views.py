from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
    RedirectView)
from django.utils import timezone
from library_app.forms import LoginForm
from library_app.models import Book


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login_url_template')


class DashboardView(LoginRequiredMixin, ListView):
    model = Book
    login_url = 'login/'
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        # data_list = [{'name': 'Jamilla', 'delta': 4, 'progress_value': 40}, ]
        if user.role == 3:
            borrowed_books = user.borrowed_books.all()
            data_list = []
            for borrowed_book in borrowed_books:
                dic = {}
                delta = borrowed_book.return_date - timezone.datetime.today().date()
                dic['book'] = borrowed_book.book.title
                dic['delta'] = delta
                days = delta.days
                if days < 1:
                    days = 1
                dic['progress_value'] = 100 // days
                data_list.append(dic)
            context['data_list'] = data_list
        return context
