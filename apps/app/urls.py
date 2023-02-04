from django.urls import path

from apps.app.views.about import about
from apps.app.views.contact import contact
from apps.app.views.home import home

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
]
