from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests

geolocator = Nominatim(user_agent="my_apps")
cities = ["Kuala Lumpur, Malaysia", "Jakarta, Indonesia", "Bangkok, Thailand", "Taipei, Taiwan", "Hong Kong",
          "Tokyo, Japan", "Beijing, China", "Seoul, South Korea"]
sentAnalysis = {"Jakarta, Indonesia": 55.4, "Bangkok, Thailand": 56.4, "Taipei, Taiwan": 51, "Hong Kong": 72.7,
                "Tokyo, Japan": 51, "Beijing, China": 47.3, "Seoul, South Korea": 48.6}


def Q3(cities, sentAnalysis):
    # a list of tuples containing latitude and longitude of all cities
    locationCoords = []

    for city in cities:
        print(city)
        location = geolocator.geocode(city)
        a = (location.latitude, location.longitude)
        locationCoords.append(a)
        print(a)

    # city name
    sortedCity = [cities[0]]
    currentCity = cities[0]
    nextCity = cities[1]

    # coordinate
    currentCoord = locationCoords[0];
    tempCoords = locationCoords

    finalShortestDistance = geodesic(locationCoords[0], locationCoords[1]).kilometers
    nextCityCoord = locationCoords[1]

    numOfCities = len(cities)

    # To get the sorted city list
    for i in range(1, numOfCities, 1):
        print("==========================================================================================")
        # Create a new dictionary
        distanceDict = {}
        # To find the nearest city
        for j in range(1, len(tempCoords), 1):
            distance = geodesic(currentCoord, tempCoords[j]).kilometers
            if distance != 0:
                print("Distance between ", currentCity, " and ", cities[j], " is ", distance, "km")
                distanceDict[cities[j]] = distance
            if distance < finalShortestDistance and distance != 0:
                nextCityCoord = tempCoords[j]
                finalShortestDistance = distance
                nextCity = cities[j]
        print("==========================================================================================")
        # Here, we have the nearest city
        print("Shortest distance : ", finalShortestDistance, "km. From ", currentCity, " to ", nextCity)
        # Now, we need to think about the conditions to select the next best city to go
        for x, y in distanceDict.items():
            if x != nextCity:
                if ((y - finalShortestDistance) / finalShortestDistance) * 100 <= 40:
                    print(sentAnalysis[nextCity])
                    print(sentAnalysis[x])
                    if sentAnalysis[nextCity] - sentAnalysis[x] >= 2:
                        loc = geolocator.geocode(x)
                        nextCityCoord = (loc.latitude, loc.longitude)
                        finalShortestDistance = y
                        nextCity = x
                        break;
        print("Latest distance : ", finalShortestDistance, "km. Recommended path is from ", currentCity, " to ",
              nextCity)
        # Steps to do after selecting the next best city to go
        tempCoords.remove(nextCityCoord)
        currentCoord = nextCityCoord
        currentCity = nextCity
        finalShortestDistance = 1000000
        cities.remove(nextCity)
        sortedCity.append(nextCity)

    print("Most Recommended destination : ", end="")
    for i in range(0, len(sortedCity), 1):
        if (i == len(sortedCity) - 1):
            print("(", sortedCity[i], ")", end="")
        else:
            print("(", sortedCity[i], ")", " --> ", end="")


Q3(cities, sentAnalysis)
