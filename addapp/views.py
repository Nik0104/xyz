from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'addinput.html')
def add(request):
    x = request.GET["t1"]
    y = request.GET["t2"]
    i = int(x)
    j = int(y)
    k = i + j
    return HttpResponse("Sum of Two Numbers is " + str(k))