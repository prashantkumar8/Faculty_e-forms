from django.conf.urls import url

from . import views

app_name = 'form'
urlpatterns = [
    url(r'^new/$', views.new, name='new'),
    url(r'^register/$', views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^(?P<person_id>[0-9]+)/$', views.person_detail, name='person_detail'),
]