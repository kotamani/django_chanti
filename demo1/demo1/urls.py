
from django.conf.urls import url
from .views import home,about

urlpatterns = [
    url('^$', home, name='home'),
    url('about', about, name='about'),
]
