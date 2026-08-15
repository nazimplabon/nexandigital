from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='dashboard/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dashboard:login'), name='logout'),
    path('', views.dashboard_home, name='home'),
    path('quotes/', views.quote_list, name='quotes'),
    path('quotes/<int:pk>/', views.quote_detail, name='quote_detail'),
    path('services/', views.service_list, name='services'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('testimonials/', views.testimonial_list, name='testimonials'),
    path('pricing/', views.pricing_list, name='pricing'),
    path('process/', views.process_list, name='process'),
    path('stats/', views.stats_list, name='stats'),
    path('blog/', views.blog_list, name='blog'),
    path('clients/', views.client_list, name='clients'),
    path('users/', views.user_list, name='users'),
]