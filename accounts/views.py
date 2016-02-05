from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def profile(request):
	return render(request, 'accounts/profile.html')

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog:index')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {
		'form': form,
		})