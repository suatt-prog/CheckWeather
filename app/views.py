from django.shortcuts import render,HttpResponse,redirect
from .models import weather
import requests
import datetime
# Create your views here.

def main(request):
    return render(request,"index.html")

def req(request):
    api_key = ""
    url = "https://api.openweathermap.org/data/2.5/weather"
    city = request.GET["city"]
    responde = requests.get(url+"?q="+city+"&appid="+api_key).json()
    currWeather = weather()
    currWeather.city = city
    currWeather.weather = responde["weather"][0]["description"]
    currWeather.date = datetime.datetime.now().date()
    currWeather.save()
    return render(request,"index.html",{"weather":responde["name"],"description":responde["weather"][0]["description"],"temperature":responde["main"]["temp"],"humidity":responde["main"]["humidity"]})