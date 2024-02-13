from django.urls import path
from .views import main_index, contact

app_name = 'main'

urlpatterns = [
    path('', main_index, name='index'),
    path('contact/', contact, name='contact'),
]