from lib.person import *

def test_person_instantiates_with_backpack():
    person = Person()

    actual = person.backpack
    expected = []

    assert actual == expected

def test_person_puts_book_in_backpack():
    person = Person()
    person.add_item_to_backpack("book")

    actual = person.backpack
    expected = ["book"]

    assert actual == expected

def test_person_puts_book_and_phone_in_backpack():
    person = Person()
    person.add_item_to_backpack("book")
    person.add_item_to_backpack("phone")

    actual = person.backpack
    expected = ["book", "phone"]

    assert actual == expected