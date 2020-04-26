import geopy.distance
import ipinfo

def get_distance(coords_1, coords_2):
    return geopy.distance.vincenty(coords_1, coords_2).km

def get_current_location():
    access_token = "88074059637b60"
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    return (details.latitude, details.longitude)

def sort_toilets(arr):
    n = len(arr)
    current_location = get_current_location()
    for i in range(n):

        for j in range(0, n-i-1):

            if get_distance(current_location, (arr[j].lat, arr[j].lon)) > get_distance(current_location, (arr[j+1].lat, arr[j+1].lon)):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr