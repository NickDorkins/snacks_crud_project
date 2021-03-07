from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template = 'snack_create.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    template = 'snack_update.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']    

class SnackDeleteView(DeleteView):
    template = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')
