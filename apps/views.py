from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("<h1>pravallika</h1>")


def myhtml(request):
    return render(request,"mypage.html")


