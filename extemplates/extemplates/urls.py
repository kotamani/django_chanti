
from django.conf.urls import url
from .views import home,about,contact,tg

urlpatterns = [
    url('^$', home),
    url('about', about, name='about'),
    url('contact', contact, name='contact'),
    url('tg', tg, name='tg'),
    url('home', home, name='home'),
]
