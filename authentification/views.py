from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
from .forms import UserCreateForm

'''def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else :
        form = UserCreateForm()
        return render(request, 'signup.html', {'form': form})'''


class signup(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


