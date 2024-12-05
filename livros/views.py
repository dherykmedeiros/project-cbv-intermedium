from django.shortcuts import render
from .models import Livro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class LivroListView(ListView): 
  model = Livro
  template_name = 'livros/livros.html'
  context_object_name = 'livros'

class LivroDetailView(DetailView):
  model = Livro
  template_name = 'livros/livro.html'

class LivroCreateView(CreateView):
  model = Livro
  fields = ['titulo', 'autor', 'editora', 'ano_publicacao','isbn','descricao']
  template_name = 'livros/criar_livro.html'
  success_url = reverse_lazy('livros')

class LivroUpdateView(UpdateView):
  model = Livro
  fields = ['titulo', 'autor', 'editora', 'ano_publicacao','isbn','descricao']
  template_name = 'livros/editar_livro.html'
  success_url = reverse_lazy('livros')

class LivroDeleteView(DeleteView):
  model = Livro
  template_name = 'livros/deletar_livro.html'
  success_url = reverse_lazy('livros')

