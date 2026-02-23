import unittest

from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def test_customer_stores_attributes(self):
        customer = Customer(1, "David", "david@example.com")
        self.assertEqual(1, customer.customer_id)
        self.assertEqual("David", customer.name)
        self.assertEqual("david@example.com", customer.email)

    def test_display_returns_expected_string(self):
        customer = Customer(2, "Ana", "ana@example.com")
        expected = "Customer ID: 2, Name: Ana, Email: ana@example.com"
        self.assertEqual(expected, customer.display())

    def test_customer_id_must_be_positive(self):
        with self.assertRaises(ValueError):
            Customer(0, "David", "david@example.com")

    def test_customer_id_must_be_int(self):
        with self.assertRaises(ValueError):
            Customer("1", "David", "david@example.com")

    def test_name_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            Customer(1, "", "david@example.com")

    def test_name_cannot_be_spaces(self):
        with self.assertRaises(ValueError):
            Customer(1, "   ", "david@example.com")

    def test_email_must_contain_at(self):
        with self.assertRaises(ValueError):
            Customer(1, "David", "david.example.com")


if __name__ == "__main__":
    unittest.main()
