from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from index.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html') 


def project(request):
    return render(request,'project.html') 


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        concern = request.POST['concern']
        country=request.POST['country']
        print(name,email,phone,concern)
        obj = Contact(name=name, phone=phone, email=email, country= country, concern=concern)
        obj.save()
        
  
        
              
    return render(request,'contact.html')
        


