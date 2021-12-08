from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http.response import JsonResponse
from django.views.generic import FormView, TemplateView, ListView, UpdateView

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

from django.urls import reverse

from .forms import UserCreateForm, UserEditForm
from .models import User

class HomeView(TemplateView):
    template_name = 'home/index.html'


class ListUsersView(ListView):
    model = User
    template_name = 'user/index.html'
    
class UserListJson(BaseDatatableView):
    model = User    
    order_columns = ['email', 'rol', 'first_name', 'last_name', 'document_number', 'birthday','telefono']
    max_display_length = 50    
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(email__contains=search)|Q(rol__contains=search)|Q(first_name__contains=search)|
                           Q(last_name__contains=search)|Q(document_number__contains=search))
        return qs
    
    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                escape(item.email),
                escape(item.rol),
                escape(item.first_name),
                escape(item.last_name),
                escape(item.document_number),
                item.birthday.strftime("%d-%m-%Y"),
                item.telefono,
                '<span class="options"><i data-url="{}" class="fas fa-edit"></i><i data-url="{}" class="{}"></i></span>'.format(
                    reverse('user-edit', args=[item.id]),
                    '',
                    'fas fa-trash' if item.is_active else 'fas fa-check'
                    )
            ])
        return json_data 
    
class CreateUserView(FormView):
    template_name = 'user/create.html'
    form_class = UserCreateForm    
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 200, 'message': 'Usuario Registrado con exito'})
    
class EditUserView(UpdateView):
    template_name = 'user/edit.html'
    form_class = UserEditForm
    model = get_user_model()  
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 200, 'message': 'Usuario Editado con exito'})