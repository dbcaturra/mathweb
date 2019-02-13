from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'mathweb/_index.html', context)
