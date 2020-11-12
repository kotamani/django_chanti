
from django.conf.urls import url
from .views import home,result


urlpatterns = [
    url('^$', home),
    url('home', home, name='home'),
    url('result', result, name='result'),
]
