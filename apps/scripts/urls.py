from django.urls import path
from .views import *

urlpatterns = [
    path('', ScriptListView.as_view(), name='scripts'),
    path('new/', ScriptCreateView.as_view(), name='new-script'),
    path('<int:pk>/', ScriptDetailView.as_view(), name='script-detail'),
    path('<int:pk>/replies/new/', LineCreateView.as_view(), name='new-line')
]