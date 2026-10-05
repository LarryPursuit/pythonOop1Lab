# Bookstore OOP Lab

Two Python classes that model items sold in a bookstore: a `Book` that can be
read online and a `Coffee` from the store's cafe. Built for the Flatiron
Object Oriented Programming (Part 1) lab.

## Features

### `Book` (`lib/book.py`)

| Member        | Description                                                              |
|---------------|--------------------------------------------------------------------------|
| `title`       | Title of the book (required).                                            |
| `page_count`  | Number of pages (required). Must be an `int`; otherwise prints `page_count must be an integer` and keeps the previous value. |
| `turn_page()` | Prints `Flipping the page...wow, you read fast!`                         |

### `Coffee` (`lib/coffee.py`)

| Member  | Description                                                                         |
|---------|-------------------------------------------------------------------------------------|
| `size`  | Required. Must be `Small`, `Medium`, or `Large`; otherwise prints `size must be Small, Medium, or Large` and keeps the previous value. |
| `price` | Price of the coffee (required).                                                      |
| `tip()` | Prints `This coffee is great, here’s a tip!` and adds `1` to `price`.               |

## Installation

Requires Python 3 and [pipenv](https://pipenv.pypa.io/).

```console
$ pipenv install
$ pipenv shell
```

## Usage

```python
from lib.book import Book
from lib.coffee import Coffee

book = Book("And Then There Were None", 272)
book.turn_page()          # Flipping the page...wow, you read fast!
book.page_count = "lots"  # page_count must be an integer

coffee = Coffee("Large", 3.50)
coffee.tip()              # This coffee is great, here’s a tip!
coffee.price              # 4.5
coffee.size = "Huge"      # size must be Small, Medium, or Large
```

`debug.py` opens an `ipdb` session with a sample `Book` for experimenting:

```console
$ python debug.py
```

## Running Tests

```console
$ pytest
```

Or run a single test file:

```console
$ pytest -x lib/testing/book_test.py
$ pytest -x lib/testing/coffee_test.py
```

## Screenshot

![All tests passing](images/tests-passing.png)

## License

See [LICENSE.md](LICENSE.md).
