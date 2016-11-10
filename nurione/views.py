from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import TcEntries
from .forms import PostForm

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.blogid = 1
			#post.published_date = timezone.now()
			post.save()
			return redirect('nurione:post_detail', pk=post.pk)
	else:
		form = PostForm()
		return render(request, 'nurione/post_edit.html', {'form' : form})

def post_list(request):
	posts = TcEntries.objects.filter(created__startswith='12').order_by('-created')[:5]
	return render(request, 'nurione/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(TcEntries, pk=pk)
	return render(request, 'nurione/post_detail.html', {'post' : post})


