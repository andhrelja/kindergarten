from django.shortcuts import render
from .models import Vrtic

# Create your views here.
def index(request):
    vrtic = Vrtic.objects.get(id=1)
    return render(request, 'vrtici/vrtic_detail.html', {'vrtic': vrtic})