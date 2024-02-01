from lib.person import *

def test_person_instantiates_with_backpack():
    person = Person()

    actual = person.backpack
    expected = []

    assert actual == expected