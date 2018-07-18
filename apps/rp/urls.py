from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    # characters
    path('characters/', CharacterListView.as_view(), name='characters'),
    path('characters/new/', CharacterCreateView.as_view(), name='new-character'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<int:pk>/edit/', CharacterUpdateView.as_view(), name='edit-character'),
    path('characters/<int:pk>/delete/', CharacterDetailView.as_view(), name='delete-character'),
    path('characters/<int:pk>/verses/new/', CharacterBioCreateView.as_view(), name='new-character-bio'),
    # verses
    path('verses/', VerseListView.as_view(), name='verses'),
    path('verses/new/', VerseCreateView.as_view(), name='new-verse'),
    path('verses/<int:pk>/', VerseDetailView.as_view(), name='verse-detail'),
    path('verses/<int:pk>/edit/', VerseUpdateView.as_view(), name='edit-verse'),
    path('verses/<int:pk>/characters/new/', VerseBioCreateView.as_view(), name='new-verse-bio'),
    # bios
    path('bios/new/', BioCreateView.as_view(), name='new-bio'),
    path('bios/<int:pk>/', BioDetailView.as_view(), name='bio-detail'),
    path('bios/<int:pk>/edit/', BioUpdateView.as_view(), name='edit-bio'),
    # traits
    path('characters/<int:pk>/traits/new/', CharacterTraitCreateView.as_view(), name='new-character-trait'),
    path('character-traits/<int:pk>/edit', CharacterTraitUpdateView.as_view(), name='edit-character-trait'),
    path('character-traits/<int:pk>/delete', CharacterTraitDeleteView.as_view(), name='delete-character-trait'),
    path('bios/<int:pk>/traits/new/', BioTraitCreateView.as_view(), name='new-bio-trait'),
    path('bio-traits/<int:pk>/edit', BioTraitUpdateView.as_view(), name='edit-bio-trait'),
    path('bio-traits/<int:pk>/delete', BioTraitDeleteView.as_view(), name='delete-bio-trait'),
    path('verses/<int:pk>/traits/new/', VerseTraitCreateView.as_view(), name='new-verse-trait'),
    path('verse-traits/<int:pk>/edit', VerseTraitUpdateView.as_view(), name='edit-verse-trait'),
    path('verse-traits/<int:pk>/delete', VerseTraitDeleteView.as_view(), name='delete-verse-trait')
]