from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, author):
    return HttpResponse("LIST OF MODS BY " + author)

def check(request, author, slug):
    return HttpResponse("Author: " + author + " Mod Name (in slug form): " + slug)
