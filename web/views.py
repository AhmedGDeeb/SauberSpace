from django.shortcuts import render
from .models import Visitor
from .utils import get_client_ip
# from .utils import get_geolocation
from .utils import days, hours

def index(request):
    ip = get_client_ip(request)
    #country, city = get_geolocation(ip)
    Visitor.objects.create(ip_address=ip) # country=country, city=city
    return render(request, 'index.html', {'days': days, 'hours': hours})