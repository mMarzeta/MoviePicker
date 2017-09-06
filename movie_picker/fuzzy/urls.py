from django.conf.urls import url
from django.conf.urls import include

from fuzzy.views import user_input


urlpatterns = [
    url(r'^$', user_input),
]
