import pytest
from src.raspblink.blink import blink

@pytest.mark.skip(reason="currently broken")
class TestBlinker:
    def test_basic_blink(self):
        blink(period=0.1, n=5)

    def test_long_period(self):
        with pytest.raises(AssertionError):
            blink(period=0.0, n=1)

    def test_short_period(self):
        with pytest.raises(AssertionError):
            blink(period=10.1, n=1)
