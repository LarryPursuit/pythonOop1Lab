#!/usr/bin/env python3

# The only sizes the store serves.
VALID_SIZES = ("Small", "Medium", "Large")


class Coffee:
    """A coffee sold in the bookstore's cafe."""

    def __init__(self, size, price):
        # Both values are required; size goes through the property setter
        # so it is validated as soon as the coffee is created.
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only accept a known size; otherwise warn and keep the previous value.
        if value in VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Tipping adds $1 to the price of the coffee.
        print("This coffee is great, here’s a tip!")
        self.price += 1
