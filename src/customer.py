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