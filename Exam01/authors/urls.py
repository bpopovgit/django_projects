# authors/urls.py
from django.urls import path
from .views import (
    AuthorCreateView, AuthorDetailView, AuthorEditView, AuthorDeleteView
)

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='create-author'),
    path('details/', AuthorDetailView.as_view(), name='details-author'),
    path('edit/', AuthorEditView.as_view(), name='edit-author'),
    path('delete/', AuthorDeleteView.as_view(), name='delete-author'),
]
