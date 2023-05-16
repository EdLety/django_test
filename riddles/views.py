from django.shortcuts import render
#from django.http import HttpResponse


def index_page(request):
    # if request.args:
    if 'name' in request.GET:
        name = request.GET['name']
        message = request.GET.get('message', '')
        template = render(request, 'hello.html', dict(name=name, message=message))
    else: 
        template = render(request, 'index.html')
    return template

#def index(request):
#    return HttpResponse("Hello, World!")
# Create your views here.
