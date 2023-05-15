from django.shortcuts import render
#from django.http import HttpResponse


def index_page(request):
    return render(request, 'index.html')
#def index(request):
#    return HttpResponse("Hello, World!")
# Create your views here.
