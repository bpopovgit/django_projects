from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from authors.models import Author
from posts.forms import PostForm
from posts.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('dashboard')  # Redirect to dashboard upon successful creation

    def form_valid(self, form):
        # Assign the first (or only) author profile to the post
        author = Author.objects.first()  # Assuming there is only one author in the system
        form.instance.author = author  # Associate the post with the author
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'details-post.html'
    context_object_name = 'post'


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit-post.html'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'post'
