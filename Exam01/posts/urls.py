# posts/urls.py
from django.urls import path
from .views import (
    PostCreateView, PostDetailView, PostEditView, PostDeleteView
)

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:pk>/details/', PostDetailView.as_view(), name='details-post'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='edit-post'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
]
