from django.db.models import Q
from django.http.response import JsonResponse
from django.views.generic import FormView, ListView, TemplateView
from django.urls.base import reverse_lazy

from django_datatables_view.base_datatable_view import BaseDatatableView

from articulo.forms import ArticuloCreateForm, CategoriaCreateForm, UnidadCreateForm

from articulo.models import Articulo, Unidad, Categoria
from user.models import User


class ListCategoriasView(TemplateView):    
    template_name = 'categoria/index.html'


class CategoriaListJson(BaseDatatableView):
    model = Categoria    
    columns = ['codigo', 'nombre', 'descripcion']
    order_columns = ['codigo', 'nombre', 'descripcion']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(codigo__contains=search)|Q(nombre__contains=search)|Q(descripcion__contains=search))
        return qs    


class CreateCategoriaView(FormView):
    template_name = 'categoria/create.html'
    form_class = CategoriaCreateForm
    success_url = reverse_lazy('user-list')
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(pk=self.request.user.id)
        form.save()
        return JsonResponse({'status': 200, 'message': 'Categoria Registrada con exito'})

    
class UnidadListJson(BaseDatatableView):
    model = Unidad
    columns = ['nombre_completo', 'nombre_corto']
    order_columns = ['nombre_completo', 'nombre_corto']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(nombre_completo__contains=search)|Q(nombre_corto__contains=search)|Q(descripcion__contains=search))
        return qs
    
    
class CreateUnidadView(FormView):
    template_name = 'unidad/create.html'
    form_class = UnidadCreateForm    
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(pk=self.request.user.id)
        form.save()
        return JsonResponse({'status': 200, 'message': 'Unidad Registrada con exito'})
    
class ArticulosView(TemplateView):
    template_name = 'articulo/index.html'
    

class ArticuloListJson(BaseDatatableView):
    model = Articulo
    columns = ['codigo', 'nombre', 'unidad', 'numero_parte']
    order_columns = ['codigo', 'nombre', 'numero_parte']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(codigo__contains=search)|Q(nombre__contains=search)|Q(numero_parte__contains=search))
        return qs


class CreateArticuloView(FormView):
    template_name = 'articulo/create.html'
    form_class = ArticuloCreateForm
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(pk=self.request.user.id)
        form.save()
        return JsonResponse({'status': 200, 'message': 'Articulo Registrado con exito'})