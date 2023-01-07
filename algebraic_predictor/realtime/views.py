from django.shortcuts import render


def counter(request):
    context = {'number': 0}
    return render(request, 'realtime/index.html', context)


def console(request):
    return render(request, 'realtime/console.html')
