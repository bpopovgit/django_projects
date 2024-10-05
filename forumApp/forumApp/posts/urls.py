from django.urls import path, include

from forumApp.posts.views import index, dashboard, add_post, delete_post, details_page, edit_post

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', delete_post, name='delete-post'),
        path('details-page/', details_page, name='details-page'),
        path('edit-post/', edit_post, name='edit-post'),
    ]))

]