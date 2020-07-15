from django.conf.urls import include
from django.urls import path
from . import views
#Add URL maps to redirect the base URL to our application
urlpatterns = [
    path('', views.library_list, name='library_list'),
]