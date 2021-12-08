from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user/list/', views.ListUsersView.as_view(), name='user-list'),
    path('user/list/data/', views.UserListJson.as_view(), name='user-list-json'),    
    path('user/create/', views.CreateUserView.as_view(), name='user-create'),
    path('user/edit/<pk>/', views.EditUserView.as_view(), name='user-edit'),
]
