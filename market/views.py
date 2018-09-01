from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'market/index.html')

def mods(request):
    return render(request, 'market/mods.html')

def textures(request):
    return render(request, 'market/textures.html')

def games(request):
    return render(request, 'market/games.html')
