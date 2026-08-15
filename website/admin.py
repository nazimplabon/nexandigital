from django.contrib import admin
from .models import (
    Service, ServiceFeature, Technology, PortfolioItem,
    BlogPost, Testimonial, SiteStat, ContactMessage,
    ClientLogo, ProcessStep, PricingPlan, PricingFeature
)

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline, TechnologyInline]

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('service',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'published_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'category')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read',)
    readonly_fields = ('created_at',)

@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'order')

class PricingFeatureInline(admin.TabularInline):
    model = PricingFeature
    extra = 1

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular', 'order')
    inlines = [PricingFeatureInline]