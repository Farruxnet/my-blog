from django.urls import path

from apps.app.views.page import page
from apps.app.views.contact import contact
from apps.app.views.home import home

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('page/<slug:slug>', page, name='page'),
]
