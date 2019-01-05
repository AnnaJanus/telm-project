from django.shortcuts import render
from django.utils import timezone
from .models import Ecgwave
from .models import File


# Create your views here.
def ecg_list(request):
    File.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'ecgsite/chart.html', {})
  return render(request, 'ecgsite/ecg_list.html', {})
