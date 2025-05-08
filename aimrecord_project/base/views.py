from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Competition
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {
       'competitions': sorted(Competition.objects.all(), key=lambda competition: competition.status == 'ended'),
    }
    return render(request, 'base/home.html', context)

def about(request):
    return render(request, 'base/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан. Вы можете войти')
            return redirect('login')
        else:
            messages.error(request, f'Ошибка создания аккаунта')
    form = UserCreationForm()
    return render(request, 'base/register.html', {'form': form})

# def get_table(request):


