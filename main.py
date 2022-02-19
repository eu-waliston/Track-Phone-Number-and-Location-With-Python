import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import Nominatim

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "pt")
print(location)
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "pt"))
key = '  ' #Go to open cage site  and take an API its free here the link https://opencagedata.com/ ^^
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=1)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Minas Gerais")
print(getLoc.address)
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)
