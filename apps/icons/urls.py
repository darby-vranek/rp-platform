from django.urls import path
from . import views

urlpatterns = [
    path('', views.IconListView.as_view(), name='icons'),
    path('fc/<int:pk>/upload/', views.IconCreateView.as_view(), name='new-icon'),
    path('new-faceclaim/', views.create_faceclaim, name='new-faceclaim'),
    path('fc/<int:pk>/', views.FaceClaimDetailView.as_view(), name='faceclaim-detail'),
    path('<int:pk>/edit/', views.IconUpdateView.as_view(), name='edit-icon'),
    path('<int:pk>/delete/', views.IconDeleteView.as_view(), name='delete-icon'),
]