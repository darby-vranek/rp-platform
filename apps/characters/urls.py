from django.urls import path
from .views import *

urlpatterns = [
    path('', CharacterListView.as_view(), name='characters'),
    path('new/', CharacterCreateView.as_view(), name='new-character'),
    path('<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('<int:pk>/edit/', CharacterUpdateView.as_view(), name='edit-character'),
    path('<int:pk>/delete/', CharacterDetailView.as_view(), name='delete-character'),
    path('<int:pk>/verses/new/', CharacterBioCreateView.as_view(), name='new-character-bio'),
    path('characters/<int:char_pk>/traits/new/', CharacterTraitCreateView.as_view(), name='new-character-trait'),
    path('characters/<int:char_pk>/traits/<int:pk>/edit/', CharacterTraitUpdateView.as_view(), name='edit-character-trait'),
    path('characters/<int:char_pk>/traits/<int:pk>/delete/', CharacterTraitDeleteView.as_view(), name='delete-character-trait'),
    path('bios/new/', BioCreateView.as_view(), name='new-bio'),
    path('bios/<int:pk>/', BioDetailView.as_view(), name='bio-detail'),
    path('bios/<int:pk>/edit/', BioUpdateView.as_view(), name='edit-bio'),
    path('verses/<int:pk>/characters/new/', VerseBioCreateView.as_view(), name='new-verse-bio'),
]