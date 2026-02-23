class Customer:
    def __init__(self, customer_id, name, email):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValueError("customer_id must be a positive integer")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

        if not isinstance(email, str) or "@" not in email or not email.strip():
            raise ValueError("email must be a valid email string")

        self.customer_id = customer_id
        self.name = name.strip()
        self.email = email.strip()

    def display(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"

import json
import os

DATA_FILE = "data/customers.json"


def load_customers(file_path=DATA_FILE):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            print("ERROR: Invalid data format in customers file.")
            return []
        return data
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON data in customers file.")
        return []


def save_customers(customers, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=2)


def create_customer(customer, file_path=DATA_FILE):
    customers = load_customers(file_path)

    customer_dict = {
        "customer_id": customer.customer_id,
        "name": customer.name,
        "email": customer.email,
    }

    customers.append(customer_dict)
    save_customers(customers, file_path)