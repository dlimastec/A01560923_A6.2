import os
import unittest

from src.hotel import Hotel, create_hotel, load_hotels


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


if __name__ == "__main__":
    unittest.main()