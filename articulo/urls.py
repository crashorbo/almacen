from django.urls import path

from . import views

urlpatterns = [
    path('parametros/', views.ListCategoriasView.as_view(), name='parametros'),
    path('categoria/list/data/', views.CategoriaListJson.as_view(), name='categoria-list'),
    path('categoria/create', views.CreateCategoriaView.as_view(), name='categoria-create'),
    path('categoria/edit/<pk>/', views.EditCategoriaView.as_view(), name='categoria-edit'),    
    path('unidad/list/data/', views.UnidadListJson.as_view(), name='unidad-list'),
    path('unidad/create', views.CreateUnidadView.as_view(), name='unidad-create'),
    path('unidad/edit/<pk>/', views.EditUnidadView.as_view(), name='unidad-edit'),
    path('', views.ArticulosView.as_view(), name='articulos'),
    path('create/', views.CreateArticuloView.as_view(), name='articulo-create'),
    path('edit/<pk>/', views.EditArticuloView.as_view(), name='articulo-edit'),
    path('list/data/', views.ArticuloListJson.as_view(), name='articulo-list'),
    path('almacen/', views.AlmacenView.as_view(), name='almacenes'),
    path('almacen/create/', views.CreateAlmacenView.as_view(), name='almacen-create'),
    path('almacen/edit/<pk>/', views.EditAlmacenView.as_view(), name='almacen-edit'),
    path('almacen/list/data/', views.AlmacenListJson.as_view(), name='almacen-list'),
    path('almacen/detail/<pk>/', views.DetailAlmacenView.as_view(), name='almacen-detail'),
]