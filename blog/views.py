from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)

	return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_detail', pk=post.pk)
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})
"""
# for electrical views

def post_list_electrical(request):
    posts_electrical = Electrical.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list_electrical.html', {'posts_electrical':posts_electrical})

def post_detail_electrical(request, pk):
    post_electrical = get_object_or_404(Electrical, pk=pk)
    return render(request, 'blog/post_detail_electrical.html', {'post_electrical': post_electrical})

@login_required
def post_new_electrical(request):
    if request.method == "POST":
        form = ElectricalForm(request.POST)
        if form.is_valid():
            post_electrical = form.save(commit=False)
            post_electrical.author = request.user
            post_electrical.published_date = timezone.now()
            post_electrical.save()
            return redirect('post_detail_electrical', pk=post_electrical.pk)
    else:
        form = ElectricalForm()
    return render(request, 'blog/post_edit_electrical.html', {'form': form})

def post_edit_electrical(request, pk):
    post_electrical = get_object_or_404(Electrical, pk=pk)
    if request.method == "POST":
        form = ElectricalForm(request.POST, instance=post_electrical)
        if form.is_valid():
            post_electrical = form.save(commit=False)
            post_electrical.author = request.user
            post_electrical.save()
            return redirect('post_detail_electrical', pk=post_electrical.pk)
    else:
        form = PostForm(instance=post_electrical)

    return render(request, 'blog/post_edit_electrical.html', {'form': form})

def post_draft_list_electrical(request):
    posts_electrical = Electrical.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list_electrical.html', {'posts_electrical': posts_electrical})

def post_publish_electrical(request, pk):
    post_electrical = get_object_or_404(Electrical, pk=pk)
    post_electrical.publish()
    return redirect('post_detail_electrical', pk=pk)

def post_remove_electrical(request, pk):
    post_electrical = get_object_or_404(Electrical, pk=pk)
    post_electrical.delete()
    return redirect('post_list_electrical')

"""