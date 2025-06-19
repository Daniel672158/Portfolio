from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Contact, Review
from django.conf import settings
from .forms import Reviewform

def home(request):
    projects = Project.objects.all().order_by('-upload_at')
    reviews = Review.objects.filter().order_by('-created_at')
    # contacts = Contact.objects.all()


    if request.method == 'POST' and 'submit-review' in request.POST:
         name = request.POST.get('name')
         message = request.POST.get('message')

         print("POST received with:", request.POST)
         if name and message:   
             Review.objects.create(name=name, message=message)
             messages.success(request, 'Review form Submitted!!!')
            #  return redirect('home')
         else:
                 messages.error(request, 'Please fill in all fields.')
        


    
    elif 'submit-contact' in request.POST:
        name = request.POST.get('name-contact')
        email = request.POST.get('email-contact')
        subject = request.POST.get('subject-contact')
        message = request.POST.get('message-contact')

        if name and email and subject and message:
            # Save to database
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # Send email
            print("Attempting to send email to:", settings.CONTACT_EMAIL)  
            full_message = f"From: {name} <{email}>\n\n{message}"
            email=EmailMessage(
                    subject=f"Portfolio Contact: {subject}",
                    body=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[email]
                                 
            )
            try:
             email.send(fail_silently=False)
             messages.success(request, 'Message sent successfully!')
            except Exception as e:
                print("Email sending failed:", e)
                messages.error(request, 'There was an error sending the email.')

    return render(request, 'blog/index.html', {
        'projects': projects,
        'reviews': reviews,
        # 'form': form ,  
        # 'contacts': contacts
          })
