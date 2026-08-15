from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, PortfolioItem, BlogPost, Testimonial, SiteStat, ContactMessage

def home(request):
    context = {
        'services': Service.objects.all(),
        'stats': SiteStat.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'website/home.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, PortfolioItem, BlogPost, Testimonial, SiteStat, ContactMessage

def home(request):
    context = {
        'services': Service.objects.all(),
        'stats': SiteStat.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'website/home.html', context)

def services(request):
    return render(request, 'website/services.html', {
        'services': Service.objects.all(),
        'stats': SiteStat.objects.all(),
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'website/service_detail.html', {'service': service})

def about(request):
    return render(request, 'website/about.html', {'stats': SiteStat.objects.all()})

def portfolio(request):
    return render(request, 'website/portfolio.html', {
        'items': PortfolioItem.objects.all(),
        'posts': BlogPost.objects.filter(is_published=True),
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:5]
    return render(request, 'website/blog_detail.html', {'post': post, 'recent_posts': recent_posts})

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        messages.success(request, "Thanks! We'll get back to you soon.")
        return redirect('website:contact')
    return render(request, 'website/contact.html')

