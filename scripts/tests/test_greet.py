import pytest
from entry import greet


def test_greet_with_valid_input():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_with_empty_string():
    assert greet("") == "Hello, !"


def test_greet_with_none():
    assert greet(None) == "Hello, None!"
