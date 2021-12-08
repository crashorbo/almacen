from django.db.models import Q
from django.http.response import JsonResponse
from django.views.generic import FormView, TemplateView
from django.urls import reverse
from django.views.generic.edit import UpdateView

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

from articulo.forms import ArticuloCreateForm, CategoriaCreateForm, UnidadCreateForm

from articulo.models import Articulo, Unidad, Categoria
from user.models import User


class ListCategoriasView(TemplateView):    
    template_name = 'categoria/index.html'


class CategoriaListJson(BaseDatatableView):
    model = Categoria        
    order_columns = ['codigo', 'nombre', 'descripcion']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(codigo__contains=search)|Q(nombre__contains=search)|Q(descripcion__contains=search))
        return qs    

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                escape(item.codigo),
                escape(item.nombre),
                escape(item.descripcion),                
                '<span class="options"><i data-url="{}" class="fas fa-edit"></i><i data-url="{}" class="{}"></i></span>'.format(
                    reverse('categoria-edit', args=[item.id]),
                    '',
                    'fas fa-trash' if not item.deleted else 'fas fa-check'
                    )
            ])
        return json_data 

class CreateCategoriaView(FormView):
    template_name = 'categoria/create.html'
    form_class = CategoriaCreateForm    
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(pk=self.request.user.id)
        form.save()
        return JsonResponse({'status': 200, 'message': 'Categoria Registrada con exito'})


class EditCategoriaView(UpdateView):
    template_name = 'categoria/edit.html'
    form_class = CategoriaCreateForm
    model = Categoria
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 200, 'message': 'Categoria Editada con exito'})

class UnidadListJson(BaseDatatableView):
    model = Unidad    
    order_columns = ['nombre_completo', 'nombre_corto']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(nombre_completo__contains=search)|Q(nombre_corto__contains=search)|Q(descripcion__contains=search))
        return qs
    
    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                escape(item.nombre_completo),
                escape(item.nombre_corto),                
                '<span class="options"><i data-url="{}" class="fas fa-edit"></i><i data-url="{}" class="{}"></i></span>'.format(
                    reverse('unidad-edit', args=[item.id]),
                    '',
                    'fas fa-trash' if not item.deleted else 'fas fa-check'
                    )
            ])
        return json_data
    
class CreateUnidadView(FormView):
    template_name = 'unidad/create.html'
    form_class = UnidadCreateForm    
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(pk=self.request.user.id)
        form.save()
        return JsonResponse({'status': 200, 'message': 'Unidad Registrada con exito'})
    
class EditUnidadView(UpdateView):
    template_name = 'unidad/edit.html'
    form_class = UnidadCreateForm
    model = Unidad
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 200, 'message': 'Unidad Editada con exito'})    

class ArticulosView(TemplateView):
    template_name = 'articulo/index.html'
    

class ArticuloListJson(BaseDatatableView):
    model = Articulo    
    order_columns = ['codigo', 'nombre', 'unidad','numero_parte']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(codigo__contains=search)|Q(nombre__contains=search)|Q(numero_parte__contains=search))
        return qs
    
    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                escape(item.codigo),
                escape(item.nombre),
                escape(item.unidad),
                escape(item.numero_parte),
                '<span class="options"><i data-url="{}" class="fas fa-edit"></i><i data-url="{}" class="{}"></i></span>'.format(
                    reverse('articulo-edit', args=[item.id]),
                    '',
                    'fas fa-trash' if not item.deleted else 'fas fa-check'
                    )
            ])
        return json_data


class CreateArticuloView(FormView):
    template_name = 'articulo/create.html'
    form_class = ArticuloCreateForm
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = User.objects.get(pk=self.request.user.id)
        form.save()
        return JsonResponse({'status': 200, 'message': 'Articulo Registrado con exito'})
    
class EditArticuloView(UpdateView):
    template_name = 'articulo/edit.html'
    form_class = ArticuloCreateForm
    model = Articulo
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 200, 'message': 'Articulo Editado con exito'})