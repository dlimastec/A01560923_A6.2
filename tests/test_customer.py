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


if __name__ == "__main__":
    unittest.main()