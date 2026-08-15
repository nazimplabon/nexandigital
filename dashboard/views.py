from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from website.models import (
    Service, PortfolioItem, ContactMessage, Testimonial,
    PricingPlan, ProcessStep, SiteStat, BlogPost, ClientLogo
)


@login_required(login_url='dashboard:login')
def dashboard_home(request):
    context = {
        'service_count': Service.objects.count(),
        'portfolio_count': PortfolioItem.objects.count(),
        'new_quotes_count': ContactMessage.objects.filter(is_read=False).count(),
        'recent_quotes': ContactMessage.objects.all()[:5],
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='dashboard:login')
def quote_list(request):
    quotes = ContactMessage.objects.all()

    search = request.GET.get('search')
    if search:
        quotes = quotes.filter(name__icontains=search)

    status = request.GET.get('status')
    if status == 'new':
        quotes = quotes.filter(is_read=False)
    elif status == 'read':
        quotes = quotes.filter(is_read=True)

    return render(request, 'dashboard/quote_list.html', {'quotes': quotes})


@login_required(login_url='dashboard:login')
def quote_detail(request, pk):
    quote = get_object_or_404(ContactMessage, pk=pk)

    if request.method == 'POST':
        if 'mark_reviewed' in request.POST:
            quote.is_read = True
            quote.save()
            messages.success(request, "Marked as reviewed.")
            return redirect('dashboard:quote_detail', pk=quote.pk)
        elif 'delete' in request.POST:
            quote.delete()
            messages.success(request, "Quote request deleted.")
            return redirect('dashboard:quotes')

    return render(request, 'dashboard/quote_detail.html', {'quote': quote})


@login_required(login_url='dashboard:login')
def service_list(request):
    services = Service.objects.all()

    search = request.GET.get('search')
    if search:
        services = services.filter(title__icontains=search)

    return render(request, 'dashboard/service_list.html', {'services': services})


@login_required(login_url='dashboard:login')
def portfolio_list(request):
    items = PortfolioItem.objects.all()

    search = request.GET.get('search')
    if search:
        items = items.filter(title__icontains=search)

    return render(request, 'dashboard/portfolio_list.html', {'items': items})


@login_required(login_url='dashboard:login')
def testimonial_list(request):
    testimonials = Testimonial.objects.all()

    search = request.GET.get('search')
    if search:
        testimonials = testimonials.filter(name__icontains=search)

    return render(request, 'dashboard/testimonial_list.html', {'testimonials': testimonials})


@login_required(login_url='dashboard:login')
def pricing_list(request):
    plans = PricingPlan.objects.all()
    return render(request, 'dashboard/pricing_list.html', {'plans': plans})


@login_required(login_url='dashboard:login')
def process_list(request):
    steps = ProcessStep.objects.all()
    return render(request, 'dashboard/process_list.html', {'steps': steps})


@login_required(login_url='dashboard:login')
def stats_list(request):
    stats = SiteStat.objects.all()
    return render(request, 'dashboard/stats_list.html', {'stats': stats})


@login_required(login_url='dashboard:login')
def blog_list(request):
    posts = BlogPost.objects.all()

    search = request.GET.get('search')
    if search:
        posts = posts.filter(title__icontains=search)

    return render(request, 'dashboard/blog_list.html', {'posts': posts})


@login_required(login_url='dashboard:login')
def client_list(request):
    clients = ClientLogo.objects.all()
    return render(request, 'dashboard/client_list.html', {'clients': clients})


@login_required(login_url='dashboard:login')
def user_list(request):
    users = User.objects.all()
    return render(request, 'dashboard/user_list.html', {'users': users})