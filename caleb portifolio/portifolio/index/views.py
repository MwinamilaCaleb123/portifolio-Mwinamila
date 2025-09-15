from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html') 

def about(request):
    return render(request,'about.html') 

def project(request):
    return render(request,'project.html') 

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        concern = request.POST['concern']
        print(name,email,phone,concern)  
        
              
    return render(request,'contact.html')
        


