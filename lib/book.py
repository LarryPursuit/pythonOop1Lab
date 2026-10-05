#!/usr/bin/env python3


class Book:
    """A book sold in the bookstore that can be read online."""

    def __init__(self, title, page_count):
        # Both values are required; page_count goes through the property setter
        # so it is validated as soon as the book is created.
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Only accept integers; otherwise warn and keep the previous value.
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
