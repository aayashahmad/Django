from django.shortcuts import render,  redirect
from .models import Contact
# from home.models import contact
from django.http import HttpResponse



# Create your views here.
def home(request):
    # return HttpResponse ("this my portfolio home page(/home)")
    context = {'name': 'Aayash','course':'Django'}
    return render(request,'home.html', context)

def about(request):
    # return HttpResponse ("this my about home page(/about)")
 return render(request,'about.html')
def projects(request):
    # return HttpResponse ("this my projects home page(/projects)")
 return render(request,'projects.html')





# def contact(request):
#     if request.method == "POST": 
#         email = request.POST['email']
#         name = request.POST['name']
#         address = request.POST['address']
#         phone = request.POST['phone']
#         desc = request.POST['desc']
        
#         contact_instance = contact(email=email, name=name, address=address, phone=phone, desc=desc)
#         contact_instance.save() 
#         print("the data has been written to the db")
#         return render(request, 'contact.html')
    
#     else:
#         return render(request, 'contact.html')

    # return HttpResponse("this my contact home page(/contact)")

    # return HttpResponse ("this my contact home page(/contact)"
 

# from django.shortcuts import render,


# views.py


# views.py
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Validate and save to the database
        if email and name and address and phone:
            Contact.objects.create(email=email, name=name, address=address, phone=phone, desc=desc)
            return HttpResponse("Form submitted successfully.")
        else:
            return HttpResponse("Form submission failed. Please fill in all fields.")

    return render(request, 'contact.html')