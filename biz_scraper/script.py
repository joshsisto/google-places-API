from place import Place
import urllib.request
import json

### https://github.com/Kyle1668/Python-Cafe-Finder/blob/master/script.py

### API call https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJY2wgNc3mmoARF6U36o7fJbg&key=AIzaSyDJjTTa_TkzBLiUT3H8AdrVbFiacijjq0k



def get_search():
    location_name = input("Enter a city and state or zip code: ")
    business_type = input("Enter business type: ")
    return location_name.replace(" ", "+"), business_type.replace(" ", "+"), print(location_name, business_type)


def return_get(location_name, business_type):
    print("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + business_type + "+near+" \
          + location_name + "&key=AIzaSyC_KZyErDtZ42CuFscO2l5YseWaV8MCHrQ&sensor=false")
    return "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + business_type + "+near+" \
          + location_name + "&key=AIzaSyC_KZyErDtZ42CuFscO2l5YseWaV8MCHrQ&sensor=false"


def places_api_request(request_url):
    web_data = urllib.request.urlopen(request_url)
    data = web_data.read()
    encoding = web_data.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))


def init_places_list(json_data):
    places = []

    if len(json_data["results"]) > 0:
        for biz_data in json_data["results"]:
            places.append(Place(biz_data))

    return places


def display_results(places_list):
    if len(places_list) > 0:
        for biz in places_list:
            biz.print_place_information()
    else:
        print("No places found")

# def place_id_info(place_id):
#     print("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + place_id + "&key=AIzaSyDJjTTa_TkzBLiUT3H8AdrVbFiacijjq0k")
#     return "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + place_id + "&key=AIzaSyDJjTTa_TkzBLiUT3H8AdrVbFiacijjq0k")


def main():
    location = get_search()
    request_url = return_get(location[0], location[1])
    json_data = places_api_request(request_url)

    places_list = init_places_list(json_data)

    display_results(places_list)
    print(json_data)


main()

