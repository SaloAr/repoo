from django.shortcuts import render

# Create your views here.
def adem(request):
    return render(request, "myApp/adm.html")