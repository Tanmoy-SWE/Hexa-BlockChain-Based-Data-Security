from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request , 'Home.html')

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'Contact.html')

def pricing(request):
    return render(request,'pricing.html')

def form(request):
    return render(request,'Form.html')
