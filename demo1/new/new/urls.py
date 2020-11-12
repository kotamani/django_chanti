
from django.conf.urls import url
from .views import say_hi

urlpatterns = [
    url('', say_hi),
]
