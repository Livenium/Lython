
import pytest

def test_add():
    from libraries.math import Math
    assert Math.add(1, 2) == 3

def test_sub():
    from libraries.math import Math
    assert Math.sub(3, 1) == 2
