from django.shortcuts import render
from sakhteman1.database import sakhtemandb

# Create your views here.

def asli(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/asli.html')
def father(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/father.html')
def call(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/call.html')
def information(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/information.html')
def signin(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/signin.html')
def sabtenam(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/sabtenam.html')
def news(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/news.html')
def payment(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/payment.html')

