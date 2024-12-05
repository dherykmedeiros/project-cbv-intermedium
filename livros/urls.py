from django.urls import path
from .views import *

urlpatterns = [
    path('', LivroListView.as_view(), name='livros'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro_detalhe'),
    path('livro/novo/', LivroCreateView.as_view(), name='livro_novo'),
    path('livro/<int:pk>/editar/', LivroUpdateView.as_view(), name='livro_atualizar'),
    path('livro/<int:pk>/excluir/', LivroDeleteView.as_view(), name='livro_excluir')
]
