# This is arin
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'name': 'arin',
        'place': 'india'
    }
    return render(request, 'index.html', data)


def analyzedtext(request):
    pass


def removepunc(request):
    text = request.GET.get('text', 'default')
    print(text)
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    if removepunc == "on":
        # analyzed = " "
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in punctuations:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_Text': analyzed
        }
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error while doing this")
