from django.shortcuts import render
from django.http import HttpResponse
from .models import Competition

competitions = [
    {
        'name': 'Кубок Стрелы Парадокса',
        'date': '18.03.24',
        'status': 'ended',
        'participants_count': 50,
        'location': 'Saint-Petersburg',
    },
    {
        'name': 'Открытый чемпионат по стрельбе из лука СПб',
        'date': '28.04.25',
        'status': 'in progress',
        'participants_count': 100,
        'location': 'Saint-Petersburg',
    }
]
# Create your views here.
def home(request):
    context = {
       'competitions': sorted(Competition.objects.all(), key=lambda competition: competition.status, reverse=True),
    }
    return render(request, 'base/home.html', context)

def about(request):
    return render(request, 'base/about.html')