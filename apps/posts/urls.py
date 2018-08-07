from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('new', PostCreateView.as_view(), name='new-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit-post'),
]