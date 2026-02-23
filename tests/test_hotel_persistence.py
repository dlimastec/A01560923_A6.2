import os
import unittest

from src.hotel import Hotel, create_hotel, load_hotels
from src.hotel import Hotel, create_hotel, load_hotels, delete_hotel


class TestHotelPersistence(unittest.TestCase):
    def setUp(self):
        self.temp_file = "data/hotels_test.json"
        with open(self.temp_file, "w", encoding="utf-8") as file:
            file.write("[]")

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_create_hotel_saves_to_file(self):
        hotel = Hotel(10, "Hotel Test", 5)
        create_hotel(hotel, self.temp_file)

        data = load_hotels(self.temp_file)
        self.assertEqual(1, len(data))
        self.assertEqual(10, data[0]["hotel_id"])
        self.assertEqual("Hotel Test", data[0]["name"])
        self.assertEqual(5, data[0]["total_rooms"])

    def test_load_hotels_returns_empty_list_if_invalid_json(self):
        with open(self.temp_file, "w", encoding="utf-8") as file:
            file.write("{ bad json")

        data = load_hotels(self.temp_file)
        self.assertEqual([], data)

    def test_delete_hotel_removes_from_file(self):
        create_hotel(Hotel(1, "H1", 5), self.temp_file)
        create_hotel(Hotel(2, "H2", 6), self.temp_file)

        deleted = delete_hotel(1, self.temp_file)
        self.assertTrue(deleted)

        data = load_hotels(self.temp_file)
        self.assertEqual(1, len(data))
        self.assertEqual(2, data[0]["hotel_id"])

    def test_delete_hotel_returns_false_if_not_found(self):
        create_hotel(Hotel(1, "H1", 5), self.temp_file)

        deleted = delete_hotel(999, self.temp_file)
        self.assertFalse(deleted)

        data = load_hotels(self.temp_file)
        self.assertEqual(1, len(data))


if __name__ == "__main__":
    unittest.main()