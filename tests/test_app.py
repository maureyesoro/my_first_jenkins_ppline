import pytest

@pytest
def test_createApp():
    x = 10
    y = 20
    z = x + y
    assert z == 30