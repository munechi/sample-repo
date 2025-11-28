import pytest
from sample_repo.main import add

def test_add():
    assert add(1, 2) == 3

def test_raise_a():
    with pytest.raises(TypeError):
        add("1", 2)

def test_raise_b():
    with pytest.raises(TypeError):
        add(1, "2")
