from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import BlogPost
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Send email
            send_mail(
                f'New contact form submission from {name}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill out all fields in the contact form.')
    
    return render(request, 'contact.html')

def blog(request):
    blog_posts = BlogPost.objects.filter(published=True).order_by('-published_date')
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug, published=True)
    return render(request, 'blog_post.html', {'post': post})

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Here you would typically save the email to your newsletter subscribers list
            # For this example, we'll just send a confirmation email
            send_mail(
                'Newsletter Subscription Confirmation',
                f'Thank you for subscribing to our newsletter with email: {email}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')  # Redirect to home page after successful subscription
        else:
            messages.error(request, 'Please provide a valid email address.')
    return redirect('home')  # Redirect back to home page if it's not a POST requestfrom django.shortcuts import render

# Create your views here.
