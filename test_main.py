import pytest
from main import Person

def test_init():
    person = Person("Alice")
    assert person.name == "Alice"

def test_str():
    person = Person("Alice")
    assert str(person) == "Alice"

def test_len():
    person = Person("Alice")
    assert len(person) == 5

def test_add():
    person_1 = Person("Alice")
    person_2 = Person("Bob")
    person_3 = person_1 + person_2
    assert str(person_3) == "AliceBob"

def test_iter():
    person = Person("Alice")
    iterator = iter(person)
    assert list(iterator) == ["A", "l", "i", "c", "e"]

def test_namezip():
    person_1 = Person("Joe")
    person_2 = Person("Bob")
    result = person_1.__namezip__(person_2)
    assert result == [("J", "B"), ("o", "o"), ("e", "b")]

def test_repr():
    person = Person("Alice")
    assert repr(person) == "Person('Alice')"

def test_lenisodd():
    person_1 = Person("Dave")
    person_2 = Person("Bob")
    assert person_1.__lenisodd__() == False
    assert person_2.__lenisodd__() == True

def test_vowelcount():
    person = Person("Alice")
    assert person.__vowelcount__() == 3

def test_capitalize():
    person = Person("alice")
    assert person.__captialize__() == "Alice"

def test_reverseit():
    person = Person("Alice")
    assert person.__reverseit__() == "ecilA"