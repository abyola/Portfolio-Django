from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')
def contact(request):
    # return HttpResponse('contact')

    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        desc =request.POST['desc']

        c= Contact(name=name, phone=phone,email=email,desc=desc)
        c.save()
    return render(request,'contact.html')