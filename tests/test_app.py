import pytest
from src.app import greet, farewell

def test_greet():
    assert greet("World") == "Welcome, World!"

def test_farewell():
    assert farewell("World") == "Goodbye, World!" 
