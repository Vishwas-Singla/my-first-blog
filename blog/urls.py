from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, UserPostListView

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    # path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
]