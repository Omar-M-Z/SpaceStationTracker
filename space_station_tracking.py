import requests
import geopy.distance
import geocoder

#returns the longitude and latitude of the ISS in that order
def iss_coords(number_only = False):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = data.get("iss_position").get("latitude")
    longitude = data.get("iss_position").get("longitude")
    if not number_only:
        if latitude[0] == "-":
            latitude = f"{latitude[1:]}º South"
        else:
            latitude = f"{latitude}º North"

        if longitude[0] == "-":
            longitude = f"{longitude[1:]}º South"
        else:
            longitude = f"{longitude}º North"
    return float(latitude), float(longitude)

#returns ground distance from current location to ISS in kilometers
def dist_to_iss():
    user_loc = geocoder.ip("me").latlng
    user_loc = (float(user_loc[0]), float(user_loc[1]))
    iss_loc = iss_coords(number_only = True)

    dist_to_iss = geopy.distance.distance(user_loc, iss_loc).km

    return round(dist_to_iss, 2)


#returns the local time at which the ISS will pass over the current location
def iss_pass_time():
    pass

#returns the time until the ISS passes over the the current location
def time_until_iss_pass():
    pass