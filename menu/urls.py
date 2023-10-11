from django.urls import path
from .views import index


urlpatterns = [
    path('home/', index, {'name': 'Home'}, name='home'),
    path('company/', index, {'name': 'About company'}, name='company'),
    path('development/', index, {'name': 'Development'}, name='development'),
    path('development/go', index, {'name': 'Development Go'}, name='development_go'),
    path('development/python', index, {'name': 'Development Python'}, name='development_python'),
    path('development/python/django', index, {'name': 'Development Python/Django'}, name='development_python_django'),
    path('prices/', index, {'name': 'Prices'}, name='prices'),
]