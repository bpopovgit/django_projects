from django.contrib import admin
from django.urls import path, include
from common.views import IndexView, DashboardView  # Import common views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Index route
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Dashboard route
    path('posts/', include('posts.urls')),  # Include posts app URLs
    path('author/', include('authors.urls')),  # Include authors app URLs
    path('admin/', admin.site.urls),
]
