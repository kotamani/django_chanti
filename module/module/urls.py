
from django.conf.urls import url
from .views import home
from design2.views import des

urlpatterns = [
    url('^$', home),
    url('design',des),
]
