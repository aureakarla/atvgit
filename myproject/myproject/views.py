from django.shortcuts import render

def aurea_view(request):
    return render(request, 'aurea.html')

def thicy_view(request):
    return render(request, 'thicy.html')
