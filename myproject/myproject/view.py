from django.http import HttpResponse

def stella_view(request):
    return HttpResponse("<h1>Funcionalidade de Stella</h1>")

def evellyn_view(request):
    return HttpResponse("<h1>Funcionalidade de Evellyn</h1>")