class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  # Currency type like "USD", "INR", etc.
        self.amount = amount  # Numerical amount

    def __repr__(self):
        return repr((self.currency, self.amount))


def __add__(self, other):
    total_amount = self.amount + other.amount
    return Currency(self.currency, total_amount)


def __add__(self, other):
    if self.currency != other.currency:
        raise ValueError("Currencies Do Not Match")
    total_amount = self.amount + other.amount
    return Currency(self.currency, total_amount)


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  # Currency type like "USD", "INR", etc.
        self.amount = amount  # Numerical amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies Do Not Match")
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


# Testing the Currency class
value1 = Currency("USD", 20)
value2 = Currency("USD", 30)
print(value1 + value2)  # Output should be ('USD', 50)

value3 = Currency("INR", 30)
try:
    print(value1 + value3)  # This should raise an exception: "Currencies Do Not Match"
except ValueError as e:
    print(e)
