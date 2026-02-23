import unittest

from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    def test_hotel_stores_attributes(self):
        hotel = Hotel(1, "Hotel One", 10)
        self.assertEqual(1, hotel.hotel_id)
        self.assertEqual("Hotel One", hotel.name)
        self.assertEqual(10, hotel.total_rooms)

    def test_display_returns_expected_string(self):
        hotel = Hotel(2, "Hotel Two", 20)
        expected = "Hotel ID: 2, Name: Hotel Two, Total Rooms: 20"
        self.assertEqual(expected, hotel.display())


if __name__ == "__main__":
    unittest.main()
