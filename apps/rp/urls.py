from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    # traits
    path('traits/<str:query>/', trait_list_view, name='traits'),
    path('traits/new/', TraitCreateView.as_view(), name='new-trait'),
]