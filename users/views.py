from django.shortcuts import render

from django.views.generic.base import RedirectView


class SwaggerRedirectView(RedirectView):
    url = 'api/swagger/'
