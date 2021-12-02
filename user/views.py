from django.http.response import JsonResponse
from django.views.generic import FormView, TemplateView, ListView
from django.urls.base import reverse_lazy

from .forms import UserCreateForm
from .models import User

class HomeView(TemplateView):
    template_name = 'home/index.html'


class ListUsersView(ListView):
    model = User
    template_name = 'user/index.html'
    
class CreateUserView(FormView):
    template_name = 'user/create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user-list')
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 200, 'message': 'Unidad Registrada con exito'})