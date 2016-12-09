from django.conf.urls import url

from . import views
  
urlpatterns = [
    url(r'^(?P<category_id>[0-9])/$', views.category, name='category'),
  
]