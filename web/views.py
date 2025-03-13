from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from datetime import datetime, time
import json

from .models import Visitor, Visits
from .utils import get_client_ip #, get_geolocation
from .utils import valid_date, valid_hour

def index(request):
    ip = get_client_ip(request)
    #country, city = get_geolocation(ip)
    Visitor.objects.create(ip_address=ip) # country=country, city=city
    return render(request, 'index.html')

@csrf_exempt # disable csrf token
def get_times(request):
     # get date
    # if request.method == 'POST':
    #     data = json.load(request.body)
    #     date_str = data.get('date')
    # if not date_str:
    #     return JsonResponse({'error': 'date parameter is required'}, status=400)
    
    try:  
        # Parse JSON data
        data = json.loads(request.body)
        date_str = data.get('date')
        print('>> getting date_str', date_str)
        if not date_str:
            return JsonResponse({'error': 'date parameter is required'}, status=400)
        today = datetime.strptime(date_str, '%Y-%m-%d').date() # Expect YYYY-MM-DD format
        print('>> today', today)
        if today < datetime.today():
            JsonResponse({'allowed_times': []})
        allowed_times = []
        _, max_allowed_hours, min_allowed_hours = valid_hour(0)
        for hour_ in range(min_allowed_hours, max_allowed_hours+1): # inclusive range
            hour = time(hour_, 0)
            current_hour = datetime.now().hour
            if today == datetime.today().date() and current_hour >= hour_:
                # check if time does not exist in DB
                continue
            if not Visits.objects.filter(date=today, hour=hour).exists():
                allowed_times.append(hour.strftime('%H:%M'))
        print('>> allowed times: ', allowed_times)
        return JsonResponse({'allowed_times': allowed_times})
    except ValueError:
        return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt  # disable csrf token
def reserve(request):
    try:
        # get date
        if request.method == 'POST':
            print(">>> request body", request.body)
            data = json.loads(request.body)
            print(">>> data", data)
            date_str = data.get('date')
            hour_str = data.get('hour')
            name = data.get('name')
            phone = date.get('phone')
            email = data.get('email')
            message = data.get('message')
            print(">>> date and hour", date_str, hour_str)
            if not date_str or not hour_str:
                return JsonResponse({'error': 'date and hour parameters are required'}, status=400)

            # check if datetime is reserved or not
            date = datetime.strptime(date_str, '%Y-%m-%d').date()  # Expect YYYY-MM-DD format
            hour = datetime.strptime(hour_str, '%H:%M').time()  # Expect HH:MM format
            visit = Visits.objects.filter(date=date, hour=hour)
            if visit.exists():
                return JsonResponse({'error': 'Visit already exists'}, status=409)
            else:
                # reserve the visit
                try:
                    Visits.objects.create(date=date, hour=hour)
                    try:
                        subject = f"meeting request at {date}-{hour} with {name}"
                        full_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

                        send_mail(
                            subject,
                            full_message,
                            'SaurbeSpace',  # From email
                            ['ahmaddeebdev@gmail.com'],   # bilalalhasan94eng@gmail.com
                        )
                    except:
                        pass  # error sending gmail
                    return JsonResponse({'message': 'Visit saved'}, status=201)
                except:
                    return JsonResponse({'error': 'Internal Server Error'}, status=500)
    except Exception as e:
        # Print exception details for debugging (optional)
        print(">>> Exception occurred:", str(e))
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
    
