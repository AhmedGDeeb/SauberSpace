def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Use a service like ipstack or ipinfo to get geographical data (e.g., country, city) based on the IP address:
# https://ipstack.com/
# https://ipinfo.io/
# import requests
# def get_geolocation(ip):
#     api_key = 'your_api_key_here'
#     response = requests.get(f"http://api.ipstack.com/{ip}?access_key={api_key}")
#     if response.status_code == 200:
#         data = response.json()
#         return data.get('country_name'), data.get('city')
#     return None, None

from datetime import datetime, timedelta
def get_working_days():
    today = datetime.now()
    working_days = []
    for i in range(30):  # Next 30 days
        day = today + timedelta(days=i)
        if day.weekday() < 5:  # 0 = Monday, 4 = Friday
            working_days.append(day)
    return working_days

days = get_working_days()
hours = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]