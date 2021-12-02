from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user/list/', views.ListUsersView.as_view(), name='user-list'),
    path('user/create/', views.CreateUserView.as_view(), name='user-create'),
]
