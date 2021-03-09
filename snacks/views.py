from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template = 'snack-list.html'
    model = Snack

class SnackDetailView(DetailView):
    template = 'snack-detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template = 'snack-create.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    

class SnackUpdateView(UpdateView):
    template = 'snack-update.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']    

class SnackDeleteView(DeleteView):
    template = 'snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')
