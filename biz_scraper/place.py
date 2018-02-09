class Place:

    def __init__(self, json_data):
        self.name = json_data["name"]
        self.place_id = json_data["place_id"]
        # self.rating = json_data["rating"]
        self.address = json_data["formatted_address"]
        # self.is_open = json_data["opening_hours"]["open_now"]

    def place_id_info(self):
        print("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + self.place_id + "&key=AIzaSyDJjTTa_TkzBLiUT3H8AdrVbFiacijjq0k")

    def print_place_information(self):
        print("--------------------------------------------------------------------")
        print("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + self.place_id + "&key=AIzaSyDJjTTa_TkzBLiUT3H8AdrVbFiacijjq0k")
        print("Place ID: " + self.place_id)
        print("Name: " + self.name)
        # print("Google Reviews Rating: " + str(self.rating))
        print("Address: " + self.address)
        # print("Is Currently Open For Business: " + str(self.is_open))




