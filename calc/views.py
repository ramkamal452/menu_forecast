from django.http import HttpResponse
import google.generativeai as genai
from django.shortcuts import render
import requests,os

def home(request):
    return render(request,'home.html')

def food(request):
  var1=(request.POST['city'])
  
  city=var1
  def get_temperature(city):
      api_key = "149b591410ad435c073aaebd469161dc"
      base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
      
      response = requests.get(base_url)
      data = response.json()
      
      if data["cod"] == 200:
          temperature = data["main"]["temp"]
          return temperature - 273.15  
      else:
          print(data)
          return None

  city = var1
  temperature = get_temperature(city)

  if temperature:
      print(f"The current temperature in {city} is {round(temperature, 2)}°C")
  else:
      print("Unable to retrieve temperature data")

  os.environ["API_KEY"] = "AIzaSyCaIKq1fZS8C1B1wv9cG_nIDbEH_fzvcqs"


  genai.configure(api_key=os.environ["API_KEY"])
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content(f"generate a menu of the food items based on the region{var1} and the temperature {temperature}")
  menu = response.candidates[0].content.parts[0].text
  formatted_menu = menu.replace("**", "<b>").replace("*", "<li>").replace("\n", "<br>")
  return render(request , 'result.html',{'formatted_menu':formatted_menu})
