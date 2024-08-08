python
from django.http import HttpResponse
from django.shortcuts import render

def aurea_view(request):
    return render(request, 'aurea.html')
