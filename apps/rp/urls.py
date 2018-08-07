from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    # verses
    path('verses/', VerseListView.as_view(), name='verses'),
    path('verses/new/', VerseCreateView.as_view(), name='new-verse'),
    path('verses/<int:pk>/', VerseDetailView.as_view(), name='verse-detail'),
    path('verses/<int:pk>/edit/', VerseUpdateView.as_view(), name='edit-verse'),
    # traits
    path('traits/<str:query>/', trait_list_view, name='traits'),
    path('traits/new/', TraitCreateView.as_view(), name='new-trait'),

    path('verses/<int:pk>/traits/new/', VerseTraitCreateView.as_view(), name='new-verse-trait'),
    path('verses/<int:verse_pk>/traits/<int:pk>/edit/', VerseTraitUpdateView.as_view(), name='edit-verse-trait'),
    path('verses/<int:verse_pk>/traits/<int:pk>/delete/', VerseTraitDeleteView.as_view(), name='delete-verse-trait'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new', PostCreateView.as_view(), name='new-post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='edit-post'),
]