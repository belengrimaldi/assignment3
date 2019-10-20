from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
   text = """<p1>welcome to my app !</p1>"""
   return HttpResponse(text)

def seatingsection(request):
   return render(request, 'seatingSection.html')

def staffmembers(request):
   text = """<h1>welcome to my app ! this is the staffmembers page</h1>"""
   return HttpResponse(text)