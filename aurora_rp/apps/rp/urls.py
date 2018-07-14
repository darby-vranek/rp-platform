from django.urls import path
from .views import *

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='characters'),
    path('characters/new/', CharacterCreateView.as_view(), name='new-character'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<int:pk>/edit/', CharacterUpdateView.as_view(), name='edit-character'),
    path('characters/<int:pk>/delete/', CharacterDetailView.as_view(), name='delete-character'),
    path('verses/', VerseListView.as_view(), name='verses'),
    path('verses/new/', VerseCreateView.as_view(), name='new-verse'),
    path('verses/<int:pk>/', VerseDetailView.as_view(), name='verse-detail'),
    path('verses/<int:pk>/edit/', VerseUpdateView.as_view(), name='edit-verse'),
    path('bios/new/', BioCreateView.as_view(), name='new-bio'),
    path('bios/<int:pk>/', BioDetailView.as_view(), name='bio-detail'),
    path('bios/<int:pk>/edit/', BioUpdateView.as_view(), name='edit-bio'),
    path('character-traits/new/', CharacterTraitCreateView.as_view(), name='new-character-trait'),
    path('character-traits/<int:pk>/edit', CharacterTraitUpdateView.as_view(), name='edit-character-trait')
]