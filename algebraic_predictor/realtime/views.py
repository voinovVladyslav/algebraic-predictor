from django.shortcuts import render


def counter(request):
    context = {'number': 0}
    return render(request, 'websockets/index.html', context)
