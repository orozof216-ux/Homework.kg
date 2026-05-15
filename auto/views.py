from django.views.generic import ListView
from . import models


class AutoListView(ListView):
    model = models.Car  
    template_name = 'cars.html'  
    context_object_name = 'cars'  

    def get_queryset(self):
        return models.Car.objects.all().order_by('-id')