import json
import os


DATA_FILE = "data/reservations.json"


class Reservation:
    def __init__(self, reservation_id, customer_id, hotel_id):
        if not isinstance(reservation_id, int) or reservation_id <= 0:
            raise ValueError("reservation_id must be a positive integer")

        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValueError("customer_id must be a positive integer")

        if not isinstance(hotel_id, int) or hotel_id <= 0:
            raise ValueError("hotel_id must be a positive integer")

        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def display(self):
        return (
            f"Reservation ID: {self.reservation_id}, "
            f"Customer ID: {self.customer_id}, Hotel ID: {self.hotel_id}"
        )


def load_reservations(file_path=DATA_FILE):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("ERROR: Invalid data format in reservations file.")
            return []

        return data
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON data in reservations file.")
        return []


def save_reservations(reservations, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(reservations, file, indent=2)


def create_reservation(reservation, file_path=DATA_FILE):
    reservations = load_reservations(file_path)

    reservation_dict = {
        "reservation_id": reservation.reservation_id,
        "customer_id": reservation.customer_id,
        "hotel_id": reservation.hotel_id,
    }

    reservations.append(reservation_dict)
    save_reservations(reservations, file_path)


def cancel_reservation(reservation_id, file_path=DATA_FILE):
    reservations = load_reservations(file_path)

    updated = [
        r
        for r in reservations
        if r.get("reservation_id") != reservation_id
    ]

    if len(updated) == len(reservations):
        return False

    save_reservations(updated, file_path)
    return True
