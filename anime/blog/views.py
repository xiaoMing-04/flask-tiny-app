from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django.contrib.auth import get_user_model
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import PostForm, MultiplePostDeleteForm
from django.contrib import messages


User = get_user_model()

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-updated_at']
    paginate_by = 8
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts_list_view.html'
    context_object_name = 'posts'
    paginate_by = 8
    
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        return Post.objects.filter(author=user).order_by('-updated_at')
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/upload.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/upload.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:home')
    
    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
    
# blog/views.py
class MultiplePostDeleteView(LoginRequiredMixin, FormView):
    template_name = 'blog/delete_multiple.html'
    form_class = MultiplePostDeleteForm
    success_url = reverse_lazy('blog:home')
    

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['queryset'] = Post.objects.filter(author=self.request.user)
        return kwargs
    

    def form_valid(self, form):
        posts_to_delete = form.cleaned_data['posts']
        for post in posts_to_delete:
            if post.author != self.request.user:
                messages.error(self.request, f"Bạn không có quyền xóa bài: {post.title}")
                return self.form_invalid(form)
            
        
        posts_to_delete.delete()
        messages.success(self.request, "Đã xóa các bài post thành công!")
        return super().form_valid(form)
    

    def form_invalid(self, form):
        messages.error(self.request, "Vui lòng chọn ít nhất một bài post để xóa.")
        return super().form_invalid(form)