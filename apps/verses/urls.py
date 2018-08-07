from django.urls import path
from .views import *

urlpatterns = [
    path('', VerseListView.as_view(), name='verses'),
    path('new/', VerseCreateView.as_view(), name='new-verse'),
    path('<int:pk>/', VerseDetailView.as_view(), name='verse-detail'),
    path('<int:pk>/edit/', VerseUpdateView.as_view(), name='edit-verse'),
    path('<int:pk>/traits/new/', VerseTraitCreateView.as_view(), name='new-verse-trait'),
    path('<int:verse_pk>/traits/<int:pk>/edit/', VerseTraitUpdateView.as_view(), name='edit-verse-trait'),
    path('<int:verse_pk>/traits/<int:pk>/delete/', VerseTraitDeleteView.as_view(), name='delete-verse-trait'),
]