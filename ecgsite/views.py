from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from django.utils import timezone
from .models import Ecgwave
from .models import File

def ecg_list(request):
    File.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'ecgsite/ecg_list.html', {})

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 dataset to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
