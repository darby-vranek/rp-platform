from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    # traits
    path('traits/<str:query>/', trait_list_view, name='traits'),
    path('traits/new/', TraitCreateView.as_view(), name='new-trait'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new', PostCreateView.as_view(), name='new-post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='edit-post'),
]