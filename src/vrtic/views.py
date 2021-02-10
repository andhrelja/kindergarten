from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'vrtici/vrtic_detail.html')

def about(request):
    return render(request, 'vrtici/vrtic_about.html')