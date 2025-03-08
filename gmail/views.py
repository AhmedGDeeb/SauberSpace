from django.core.mail import send_mail
from django.shortcuts import render

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Inquiry from {name}"
        full_message = f"Name: {name}\nPhone: {phone}\nService: {service}\nEmail: {email}\nMessage: {message}"

        send_mail(
            subject,
            full_message,
            'SaurbeSpace',  # From email
            ['bilalalhasan94eng@gmail.com'],   # To email(s) b
        )
    return render(request, 'index.html')  # Fallback to contact page
