import phonenumbers 
from myPhone import number
import opencage
import folium

from phonenumbers import geocoder


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "es")
print(location)

from phonenumbers import carrier
serviceProv = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProv,"es"))

from opencage.geocoder import OpenCageGeocode

key = "134513698ed445a79b7cc6920a307db9"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")