from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    name="ramakrishna"
    return render(request,'hi.html',{'n':name})
def next(request):
    return render(request,'tq.html')
