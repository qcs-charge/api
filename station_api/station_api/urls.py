from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('lk/', admin.site.urls),
    path('', include('main.urls')),
]
