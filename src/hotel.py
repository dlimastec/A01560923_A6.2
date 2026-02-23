import json
import os


DATA_FILE = "data/hotels.json"


class Hotel:
    def __init__(self, hotel_id, name, total_rooms):
        if not isinstance(hotel_id, int) or hotel_id <= 0:
            raise ValueError("hotel_id must be a positive integer")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

        if not isinstance(total_rooms, int) or total_rooms <= 0:
            raise ValueError("total_rooms must be a positive integer")

        self.hotel_id = hotel_id
        self.name = name.strip()
        self.total_rooms = total_rooms

    def display(self):
        return (
            f"Hotel ID: {self.hotel_id}, Name: {self.name}, Total Rooms: {self.total_rooms}"
        )


def load_hotels(file_path=DATA_FILE):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("ERROR: Invalid data format in hotels file.")
            return []

        return data
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON data in hotels file.")
        return []


def save_hotels(hotels, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(hotels, file, indent=2)


def create_hotel(hotel, file_path=DATA_FILE):
    hotels = load_hotels(file_path)

    hotel_dict = {
        "hotel_id": hotel.hotel_id,
        "name": hotel.name,
        "total_rooms": hotel.total_rooms,
    }

    hotels.append(hotel_dict)
    save_hotels(hotels, file_path)

def delete_hotel(hotel_id, file_path=DATA_FILE):
    hotels = load_hotels(file_path)

    updated = [h for h in hotels if h.get("hotel_id") != hotel_id]

    if len(updated) == len(hotels):
        return False

    save_hotels(updated, file_path)
    return True

def get_hotel(hotel_id, file_path=DATA_FILE):
    hotels = load_hotels(file_path)

    for hotel in hotels:
        if hotel.get("hotel_id") == hotel_id:
            return hotel

    return None

def update_hotel(hotel_id, name=None, total_rooms=None, file_path=DATA_FILE):
    if name is not None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

    if total_rooms is not None:
        if not isinstance(total_rooms, int) or total_rooms <= 0:
            raise ValueError("total_rooms must be a positive integer")

    hotels = load_hotels(file_path)

    for hotel in hotels:
        if hotel.get("hotel_id") == hotel_id:
            if name is not None:
                hotel["name"] = name.strip()
            if total_rooms is not None:
                hotel["total_rooms"] = total_rooms

            save_hotels(hotels, file_path)
            return True

    return False