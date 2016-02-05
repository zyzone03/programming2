from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'blog/index.html', {})

def post_list(request):
	post_list = Post.objects.all()
	return render(request, 'blog/post_list.html', {
		'post_list': post_list
		})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	params = {'post': post}
	return render(request, 'blog/post_detail.html', params)


def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save()
			return redirect(post)
	else:
		form = PostForm()
	return render(request, 'blog/post_new.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(post)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_new.html', {'form':form})


def comment_new(request, post_pk):
	# post = get_object_or_404(Post, post_pk=post_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = get_object_or_404(Post, pk=post_pk)
			comment.save()
			messages.debug(request, 'new 댓글 등록됨')
			return redirect('blog:post_detail', post_pk)
	else:
		form = CommentForm()
	return render(request, 'blog/comment_new.html', {
		'form':form,
		})

def comment_edit(request, post_pk, pk):
	comment = get_object_or_404(Comment, pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return redirect('blog:post_detail', post_pk)
	else:
		form = CommentForm(instance=comment)
	return render(request, 'blog/comment_new.html', {
		'form':form,
		})
