from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')


def nomepage(request):
    return render(request,'myapp/layouts-normal.html')


def hidden_sidebar(request):
    return render(request,'myapp/layouts-hidden-sidebar.html')


def fixed_sidebar(request):
    return render(request,'myapp/layouts-fixed-sidebar.html')


def fixed_header(request):
    return render(request,'myapp/layouts-fixed-header.html')
