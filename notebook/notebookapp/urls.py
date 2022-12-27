from django.urls import path

from . import views

urlpatterns = [
	path('', views.homePageView, name='home'),
	path('list', views.listView, name='list'),
]
