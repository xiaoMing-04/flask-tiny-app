from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, MultiplePostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/multiple_post_delete/', MultiplePostDeleteView.as_view(), name='multiple_post_delete')
]