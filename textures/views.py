from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, author):
    return HttpResponse("LIST OF TEXTURES BY " + author)

def check(request, author, slug):
    return HttpResponse("Author: " + author + " Texture Name (in slug form): " + slug)
