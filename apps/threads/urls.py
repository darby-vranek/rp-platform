from django.urls import path
from .views import *

urlpatterns = [
    # threads
    path('', ThreadListView.as_view(), name='threads'),
    path('new/', ThreadCreateView.as_view(), name='new-thread'),
    path('<int:pk>/', ThreadDetailView.as_view(), name='thread-detail'),
    path('<int:pk>/edit/', ThreadUpdateView.as_view(), name='edit-thread'),
    path('<int:pk>/delete/', ThreadDeleteView.as_view(), name='delete-thread'),
    # replies
    path('<int:pk>/replies/new/', ReplyCreateView.as_view(), name='new-reply'),
    path('<int:thread_pk>/replies/<int:pk>/edit/', ReplyUpdateView.as_view(), name='edit-reply'),
    path('<int:thread_pk>/replies/<int:pk>/delete/', ReplyDeleteView.as_view(), name='delete-reply'),
]