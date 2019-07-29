from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_shows),
    url(r'^show$', views.all_shows),
    # url(r'^edit_show$', views.edit_show),   
    url(r'^show/new$', views.new_show),
    # url(r'^show_detail$', views.show_detail),
    url(r'^show/(?P<show_id>\d+)/edit$',views.edit_show),
    url(r'^show/(?P<show_id>\d+)/update$',views.update_show),
    url(r'^show/(?P<show_id>\d+)$',views.show_detail),
    url(r'^show/create$',views.create_show),
    url(r'^show/(?P<show_id>\d+)/destroy$',views.destroy_show),
]
# url(r'^register/$', 'register', name='urlname')