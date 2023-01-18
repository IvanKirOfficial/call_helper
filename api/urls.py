from django.urls import path, include

from api.spectacular.urls import urlpatterns as swagger_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += swagger_urls
