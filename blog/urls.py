from django.conf.urls import include
from django.urls import path
from . import views
# Here we're importing Django's function path and all of our views from the blog application.
# After that, we can add our first URL pattern:
# blog/urls.py
urlpatterns = [
    path('', views.post_list, name='post_list'),
]