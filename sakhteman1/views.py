from django.shortcuts import render
from sakhteman1.database import sakhtemandb

# Create your views here.

def asli(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/asli.html')
def father(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/father.html')
