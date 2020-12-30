from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm,CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    
    redirect_field_name = 'blogapp:post_list'
    model = Post
    form_class = PostForm

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
   
    redirect_field_name = 'blogapp:post_list'
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp:post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('blogapp:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogapp/comment_form.html', {'form': form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blogapp:post_detail', pk=post_pk)


