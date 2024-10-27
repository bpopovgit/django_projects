from django.views.generic import TemplateView, ListView
from posts.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'  # Template for the homepage


class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'
    context_object_name = 'posts'  # Posts will be accessible in the template as 'posts'
