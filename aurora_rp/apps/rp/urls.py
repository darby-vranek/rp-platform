from django.urls import path
from .views import *

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='characters'),
    path('characters/new/', CharacterCreateView.as_view(), name='new-character'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<int:pk>/edit/', CharacterUpdateView.as_view(), name='edit-character'),
    path('characters/<int:pk>/delete/', CharacterDetailView.as_view(), name='delete-character')
]