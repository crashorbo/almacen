from django.urls import path

from . import views

urlpatterns = [
    path('parametros/', views.ListCategoriasView.as_view(), name='parametros'),
    path('categoria/list/data/', views.CategoriaListJson.as_view(), name='categoria-list'),
    path('categoria/create', views.CreateCategoriaView.as_view(), name='categoria-create'),    
    path('unidad/list/data/', views.UnidadListJson.as_view(), name='unidad-list'),
    path('unidad/create', views.CreateUnidadView.as_view(), name='unidad-create'),
    path('', views.ArticulosView.as_view(), name='articulos'),
    path('create/', views.CreateArticuloView.as_view(), name='articulo-create'),
    path('list/data/', views.ArticuloListJson.as_view(), name='articulo-list'),
]