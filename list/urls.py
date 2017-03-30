from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_pattens

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^list/', views.list, name='list'),
	url(r'^admin/', views.admin, name='admin')

	# API urls
	url(r'^bothers/$', views.BrothersList.as_view()),
	url(r'^brothers/(?P<pk>[0-9]+)/$', views.BrothersDetail.as_view()),

	url(r'^guests/$', views.GuestList.as_view()),
	url(r'^guests/(?P<pk>[0-9]+)/$', views.GuetsDetail.as_view()),

	url(r'^users/$', views.UsersList.as_view()),
	url(r'^usersList/(?P<pk>[0-9]+)/$', views.UsersDetail.as_view()),

]

urlpatterns = format_suffix_pattens(urlpatterns)
