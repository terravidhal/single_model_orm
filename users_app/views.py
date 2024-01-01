from django.shortcuts import render, HttpResponse #  import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")