#!/usr/bin/python3.6
import pyowm

owm = pyowm.OWM('ab23472268a7106bfac409139f594452', language="ru")

place = input("Ваш город ?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура в районе " + str(temp))

if temp < 10:
    print("На улице холодно...одевайтесь теплее.")
elif temp < 20:
    print("На улице холодно")
elif temp < 30:
    print("На улице не холодно но и не жарко")
else:
    print("На улице жарко")

end_command = input("Press any key to exit...")

