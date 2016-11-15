from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "disappearingninjas/index.html")

def ninja(request, ninja):
    context = {
        'ninja' : ninja
    }
    return render(request, "disappearingninjas/show_ninja.html", context)
