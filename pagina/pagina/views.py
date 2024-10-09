from django.shortcuts import render
def home(request):
    return render(request,'home.html',{})
def contenidoDinamico(request, name):
    context = {'name': name}
    return render (request, 'contenidoDinamico.html', context)
