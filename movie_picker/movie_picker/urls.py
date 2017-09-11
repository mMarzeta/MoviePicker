from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fuzzy/', include('movie_picker.fuzzy.urls', namespace='movie_picker.fuzzy')),
]
