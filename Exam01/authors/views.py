from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from authors.forms import CreateAuthorForm, EditAuthorForm
from authors.models import Author
from posts.models import Post


class AuthorCreateView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'create-author.html'
    success_url = reverse_lazy('dashboard')  # Redirects to the dashboard on success


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'details-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        try:
            return Author.objects.get()
        except Author.DoesNotExist:
            raise Http404("No Author profile found.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(author=self.object)
        context['total_posts'] = posts.count()

        latest_post = posts.order_by('-updated_at').first()
        context['latest_post_title'] = latest_post.title if latest_post else "N/A"

        return context


class AuthorEditView(UpdateView):
    model = Author
    form_class = EditAuthorForm
    template_name = 'edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        # Assuming there's only one author profile in the system, retrieve it without needing a pk or slug
        return Author.objects.first()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'delete-author.html'
    success_url = reverse_lazy('index')  # Redirect to index after deletion

    def get_object(self, queryset=None):
        author = Author.objects.first()
        if author is None:
            raise Http404("No author profile found.")
        return author

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        Post.objects.filter(author=self.object).delete()
        return super().delete(request, *args, **kwargs)