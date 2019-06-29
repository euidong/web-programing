from django.shortcuts import render
from .models import Notice

# Create your views here.

def test_view(request) :
    notices = Notice.objects.all()
    context = {'notices':notices}
    return render(request, 'main.html', context)