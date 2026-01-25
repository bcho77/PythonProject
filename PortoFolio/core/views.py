from django.core.mail import  send_mail
from django.shortcuts import render
from django.http import Http404
from .form import ContactForm
from django.conf import settings


ALLOWED_TUTORIALS = ["docker", "devops", "terraform", "kubernetes", "network", "python"]
# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def projects(request):
    return render(request, 'core/projects.html')

def tutorial(request): 
    return render(request, 'core/tutorial.html')


# def tutorial_detail(request, topic):

#     template_name = f"core/tutorial/{topic}.html"

#     try:
#         return render(request, template_name)
#     except:
#         raise Http404("Tutorial not found")
    

def tutorial_detail(request, topic):
    if topic not in ALLOWED_TUTORIALS:
        raise Http404()
    return render(request, f"core/tutorial/{topic}.html")
    


def contact(request):
    if request.method == 'POST':
         # Handle form submission logic here
        form = ContactForm(request.POST)
        if form.is_valid():
             # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #  subject = form.cleaned_data['subject']
            #  phone = form.cleaned_data.get('phone')
            #  attachment = form.cleaned_data.get('attachment')
             
             # You can add logic to send an email or save the data to the database here
            full_message = f"Message from {name} ({email}):\n\n{message}"
        
            send_mail(
                subject= "New Contact Form Message",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["djiofnoel@gmail.com"]
            )

            return render(request, "core/contact.html",{
                "form": ContactForm(),
                "success": True 
            })
        
            # return redirect("contact")
                
    else:
        form = ContactForm()

           
    return render(request, 'core/contact.html', {'form': form})
