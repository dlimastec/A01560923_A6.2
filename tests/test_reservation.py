import unittest

from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    def test_reservation_stores_attributes(self):
        r = Reservation(1, 10, 20)
        self.assertEqual(1, r.reservation_id)
        self.assertEqual(10, r.customer_id)
        self.assertEqual(20, r.hotel_id)

    def test_display_returns_expected_string(self):
        r = Reservation(2, 11, 21)
        expected = "Reservation ID: 2, Customer ID: 11, Hotel ID: 21"
        self.assertEqual(expected, r.display())


if __name__ == "__main__":
    unittest.main()
