
import pytest

def test_greet():
    from contracts.example import Example
    example = Example()
    assert example.greet() == "Hello, Livenium ⊽!"
