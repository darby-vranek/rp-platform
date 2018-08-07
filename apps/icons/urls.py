from django.urls import path
from . import views

urlpatterns = [
    path('', views.IconListView.as_view(), name='icons'),
    path('new/', views.IconCreateView.as_view(), name='new-icon'),
    path('fc/<slug:name>/', views.IconFcList, name='fc-icons'),
    path('<int:pk>/edit/', views.IconUpdateView.as_view(), name='edit-icon'),
    path('<int:pk>/delete/', views.IconDeleteView.as_view(), name='delete-icon'),
]