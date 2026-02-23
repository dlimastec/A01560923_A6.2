import os
import unittest

from src.hotel import Hotel, create_hotel, reserve_room
from src.reservation import load_reservations
from src.hotel import Hotel, create_hotel, reserve_room, cancel_hotel_reservation, load_hotels


class TestHotelReservation(unittest.TestCase):
    def setUp(self):
        self.hotels_file = "data/hotels_test_reserve.json"
        self.res_file = "data/reservations_test_reserve.json"

        with open(self.hotels_file, "w", encoding="utf-8") as f:
            f.write("[]")
        with open(self.res_file, "w", encoding="utf-8") as f:
            f.write("[]")

    def tearDown(self):
        if os.path.exists(self.hotels_file):
            os.remove(self.hotels_file)
        if os.path.exists(self.res_file):
            os.remove(self.res_file)

    def test_reserve_room_creates_reservation_and_increments_reserved(self):
        create_hotel(Hotel(1, "H1", 1), self.hotels_file)

        ok = reserve_room(
            reservation_id=100,
            customer_id=10,
            hotel_id=1,
            hotels_file_path=self.hotels_file,
            reservations_file_path=self.res_file,
        )
        self.assertTrue(ok)

        reservations = load_reservations(self.res_file)
        self.assertEqual(1, len(reservations))
        self.assertEqual(100, reservations[0]["reservation_id"])

    def test_reserve_room_fails_if_no_rooms_available(self):
        create_hotel(Hotel(1, "H1", 1), self.hotels_file)

        ok1 = reserve_room(100, 10, 1, self.hotels_file, self.res_file)
        ok2 = reserve_room(101, 11, 1, self.hotels_file, self.res_file)

        self.assertTrue(ok1)
        self.assertFalse(ok2)

    def test_cancel_hotel_reservation_removes_reservation_and_decrements_reserved(self):
        create_hotel(Hotel(1, "H1", 2), self.hotels_file)

        ok = reserve_room(200, 10, 1, self.hotels_file, self.res_file)
        self.assertTrue(ok)

        cancelled = cancel_hotel_reservation(200, self.hotels_file, self.res_file)
        self.assertTrue(cancelled)

        reservations = load_reservations(self.res_file)
        self.assertEqual([], reservations)

        hotels = load_hotels(self.hotels_file)
        self.assertEqual(0, hotels[0].get("reserved_rooms", 0))

    def test_cancel_hotel_reservation_returns_false_if_reservation_not_found(self):
        create_hotel(Hotel(1, "H1", 2), self.hotels_file)

        cancelled = cancel_hotel_reservation(999, self.hotels_file, self.res_file)
        self.assertFalse(cancelled)


if __name__ == "__main__":
    unittest.main()