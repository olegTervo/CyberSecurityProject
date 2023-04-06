from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('list/<str:user_id>', views.listView, name='list'),
    path('add', views.addView, name='add'),
]
