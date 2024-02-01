from lib.person import *
import pytest

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

def test_person_puts_empty_string_into_backpack():
    person = Person()
    with pytest.raises(Exception) as e:
        person.add_item_to_backpack("")

    actual = str(e.value)
    expected = "Please provide an item to put in the backpack!"

    assert actual == expected