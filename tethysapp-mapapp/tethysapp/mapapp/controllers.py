from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button



@login_required()
def home(request):
    context = {

    }

    return render(request, 'mapapp/home.html', context)

@login_required()
def bufferrings(request):
    context = {

    }

    return render(request, 'mapapp/bufferrings.html', context)

@login_required()
def bufferpop(request):
    context = {

    }

    return render(request, 'mapapp/bufferpop.html', context)

@login_required()
def about(request):
    context = {

    }

    return render(request, 'mapapp/about.html', context)