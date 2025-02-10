from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'registration.html')

# Create your views here.
