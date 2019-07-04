from django.shortcuts import render
from .models import Notice

# Create your views here.

def notice_view(request) :
    notices = Notice.objects.all()
    context = {'notices':notices}
    return render(request, 'notice.html', context)
    