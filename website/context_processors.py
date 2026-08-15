from .models import Service

def nav_services(request):
    return {'nav_services': Service.objects.all()}