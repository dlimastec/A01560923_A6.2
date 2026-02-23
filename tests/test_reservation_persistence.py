import os
import unittest

from src.reservation import (
    Reservation,
    cancel_reservation,
    create_reservation,
    load_reservations,
)


class TestReservationPersistence(unittest.TestCase):
    def setUp(self):
        self.temp_file = "data/reservations_test.json"
        with open(self.temp_file, "w", encoding="utf-8") as file:
            file.write("[]")

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_create_reservation_saves_to_file(self):
        r = Reservation(10, 1, 2)
        create_reservation(r, self.temp_file)

        data = load_reservations(self.temp_file)
        self.assertEqual(1, len(data))
        self.assertEqual(10, data[0]["reservation_id"])
        self.assertEqual(1, data[0]["customer_id"])
        self.assertEqual(2, data[0]["hotel_id"])

    def test_load_reservations_returns_empty_list_if_invalid_json(self):
        with open(self.temp_file, "w", encoding="utf-8") as file:
            file.write("{ bad json")

        data = load_reservations(self.temp_file)
        self.assertEqual([], data)

    def test_cancel_reservation_removes_from_file(self):
        create_reservation(Reservation(1, 10, 20), self.temp_file)
        create_reservation(Reservation(2, 11, 21), self.temp_file)

        cancelled = cancel_reservation(1, self.temp_file)
        self.assertTrue(cancelled)

        data = load_reservations(self.temp_file)
        self.assertEqual(1, len(data))
        self.assertEqual(2, data[0]["reservation_id"])

    def test_cancel_reservation_returns_false_if_not_found(self):
        create_reservation(Reservation(1, 10, 20), self.temp_file)

        cancelled = cancel_reservation(999, self.temp_file)
        self.assertFalse(cancelled)

        data = load_reservations(self.temp_file)
        self.assertEqual(1, len(data))


if __name__ == "__main__":
    unittest.main()
