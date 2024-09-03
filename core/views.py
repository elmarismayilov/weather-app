from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            try:
                city_name = city
                print(city_name)
                k = '37f7c915f8aa49ff9b6130344240309'
                response = requests.get('https://api.weatherapi.com/v1/current.json', params=dict(key=k, q=city_name))
                data = response.json()
                weather_data = {
                    'city': data['location']['name'],
                    'temperature': data['current']['temp_c'],
                    'humidity': data['current']['humidity'],
                    'conditions': data['current']['condition']['text'],
                    'wind_speed': data['current']['wind_kph']
                }
                print(weather_data)
                return render(request, 'index.html', weather_data)
            except KeyError:
                return render(request,"index.html", {'error': 'Invalid city name.'})
        else:
            return render(request, 'index.html', {'error': 'Please enter a city name.'})
    if request.method == "GET":
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'who-we-are.html')