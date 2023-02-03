from django.urls import path
from main import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('attribution/', views.attribution, name='attribution'),
    path('debug/', views.api_debug, name='api_debug'),
    path('gallery/', views.gallery, name='gallery'),
    path('live/', views.live_view, name='live_view'),
    path('source/', views.source, name='source'),
    
    path('api/', views.api_docs, name='api'),
    path('api/flight/', views.api_flight, name='api_flight'),
    path('api/station/', views.api_station, name='api_station'),
    path('docs/', views.api_docs, name='api_docs'),
]
