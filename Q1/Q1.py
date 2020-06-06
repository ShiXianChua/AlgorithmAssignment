from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
from gmplot import gmplot

geolocator = Nominatim(user_agent="my_apps")
places = ["Kuala Lumpur, Malaysia","Jakarta, Indonesia","Bangkok, Thailand","Taipei, Taiwan","Hong Kong","Tokyo, Japan","Beijing, China","Seoul, South Korea"]

# all latitude and longitude of all cities
locationArr = []


def Q1():
    for i in places:
        location = geolocator.geocode(i)
        print(i)

        a = (location.latitude,location.longitude)
        locationArr.append(a)
        print(a)

    # key reference
    keyD = geodesic(locationArr[0],locationArr[1]).kilometers
    keyL = locationArr[1]

    # city name
    storeCityName =[places[0]]
    checkLName = places[0]
    place = places[1]
    # coordinate
    checkCoordinate = locationArr[0];
    storeAddress = [locationArr[0]]
    tempPlaces = locationArr

    for i in range(1,len(places),1):
        print("==========================================================================================")
        for j in range(1,len(tempPlaces),1):
            distance = geodesic(checkCoordinate,tempPlaces[j]).kilometers
            if (distance != 0):
                print("Distance between ", checkLName, " and ", places[j], " is ", distance, "km")
            if(distance<keyD and distance !=0):
                keyL = tempPlaces[j]
                keyD = distance
                place = places[j]
        print("==========================================================================================")
        print("Shortest distance : ", keyD, "km . Next destination from ",checkLName," to ", place)
        tempPlaces.remove(keyL)
        checkCoordinate = keyL
        checkLName = place
        keyD = 1000000
        places.remove(place)
        storeCityName.append(place)
        storeAddress.append(keyL)

    print("Recommended destination : ",end ="")
    for i in range (0,len(storeCityName),1):
        if(i==len(storeCityName)-1):
            print("(",storeCityName[i],")",end="")
        else:
            print("(",storeCityName[i],")" ," --> ", end ="")

    gmap = gmplot.GoogleMapPlotter(3.1516964, 101.6942371, 3)
    gmap.apikey = "AIzaSyD3cSr8TLouz71dNLj - VBMnacep2ChcFLM"

    # split longitude and laatitude
    latitude = [x for x, y in storeAddress]
    longitude = [y for x, y in storeAddress]

    gmap.scatter(latitude, longitude, colour='red', size=40, marker=False)
    gmap.polygon(latitude, longitude, colour='cornflowerblue')
    gmap.draw("myMapQ1.html")


Q1();