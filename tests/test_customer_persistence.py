import os
import unittest

from src.customer import (
    Customer,
    create_customer,
    delete_customer,
    get_customer,
    load_customers,
    update_customer,
)


class TestCustomerPersistence(unittest.TestCase):
    def setUp(self):
        self.temp_file = "data/customers_test.json"
        with open(self.temp_file, "w", encoding="utf-8") as file:
            file.write("[]")

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_create_customer_saves_to_file(self):
        customer = Customer(10, "Ana", "ana@example.com")
        create_customer(customer, self.temp_file)

        data = load_customers(self.temp_file)
        self.assertEqual(1, len(data))
        self.assertEqual(10, data[0]["customer_id"])
        self.assertEqual("Ana", data[0]["name"])
        self.assertEqual("ana@example.com", data[0]["email"])

    def test_load_customers_returns_empty_list_if_invalid_json(self):
        with open(self.temp_file, "w", encoding="utf-8") as file:
            file.write("{ bad json")

        data = load_customers(self.temp_file)
        self.assertEqual([], data)

    def test_delete_customer_removes_from_file(self):
        create_customer(Customer(1, "A", "a@a.com"), self.temp_file)
        create_customer(Customer(2, "B", "b@b.com"), self.temp_file)

        deleted = delete_customer(1, self.temp_file)
        self.assertTrue(deleted)

        data = load_customers(self.temp_file)
        self.assertEqual(1, len(data))
        self.assertEqual(2, data[0]["customer_id"])

    def test_delete_customer_returns_false_if_not_found(self):
        create_customer(Customer(1, "A", "a@a.com"), self.temp_file)

        deleted = delete_customer(999, self.temp_file)
        self.assertFalse(deleted)

        data = load_customers(self.temp_file)
        self.assertEqual(1, len(data))

    def test_get_customer_returns_customer_if_found(self):
        create_customer(Customer(5, "Eva", "eva@eva.com"), self.temp_file)

        customer = get_customer(5, self.temp_file)
        self.assertIsNotNone(customer)
        self.assertEqual(5, customer["customer_id"])
        self.assertEqual("Eva", customer["name"])

    def test_get_customer_returns_none_if_not_found(self):
        create_customer(Customer(5, "Eva", "eva@eva.com"), self.temp_file)

        customer = get_customer(999, self.temp_file)
        self.assertIsNone(customer)

    def test_update_customer_updates_name_and_email(self):
        create_customer(Customer(7, "Old", "old@old.com"), self.temp_file)

        updated = update_customer(
            7, name="New", email="new@new.com", file_path=self.temp_file
        )
        self.assertTrue(updated)

        customer = get_customer(7, self.temp_file)
        self.assertEqual("New", customer["name"])
        self.assertEqual("new@new.com", customer["email"])

    def test_update_customer_returns_false_if_not_found(self):
        create_customer(Customer(7, "Old", "old@old.com"), self.temp_file)

        updated = update_customer(999, name="New", file_path=self.temp_file)
        self.assertFalse(updated)

    def test_update_customer_raises_valueerror_on_invalid_email(self):
        create_customer(Customer(7, "Old", "old@old.com"), self.temp_file)

        with self.assertRaises(ValueError):
            update_customer(7, email="invalid-email", file_path=self.temp_file)


if __name__ == "__main__":
    unittest.main()
