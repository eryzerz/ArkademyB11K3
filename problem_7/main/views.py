from django.urls import reverse_lazy
from django.views.generic import ListView
from bootstrap_modal_forms.generic import BSModalLoginView, BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from .forms import NameForm
from .models import Name
# Create your views here.

class Index(ListView):
    model = Name
    context_object_name = 'employees'
    template_name = 'index.html'

class EntryCreateView(BSModalCreateView):
    template_name ='main/create_entry.html'
    form_class = NameForm
    success_message = 'Success: Entry was created.'
    success_url = reverse_lazy('index')

class EntryUpdateView(BSModalUpdateView):
    model = Name
    template_name = 'main/update_entry.html'
    form_class = NameForm
    success_message = 'Success: Entry was updated.'
    success_url = reverse_lazy('index')


class EntryDeleteView(BSModalDeleteView):
    model = Name
    template_name = 'main/delete_entry.html'
    success_message = 'Success: Entry was deleted.'
    success_url = reverse_lazy('index')