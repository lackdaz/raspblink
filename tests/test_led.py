import pytest
from src.raspblink.led import LED


@pytest.fixture
def led_fixture():
    return LED()


class TestLED:
    def test_led_can_switch_on_at_default(self, led_fixture):
        led_fixture.switch_on()
        assert led_fixture.duty_cycle == 1e6

    def test_led_can_switch_off_at_default(self, led_fixture):
        led_fixture.switch_off()
        assert led_fixture.duty_cycle == 0

    def test_led_can_switch_on_at_zero(self, led_fixture):
        led_fixture.switch_on(duty_cycle=0.0)
        assert led_fixture.duty_cycle == 0

    def test_led_can_switch_on_at_half(self, led_fixture):
        led_fixture.switch_on(duty_cycle=50.0)
        assert led_fixture.duty_cycle == 5e5

    def test_led_can_switch_on_at_full(self, led_fixture):
        led_fixture.switch_on(duty_cycle=100.0)
        assert led_fixture.duty_cycle == 1e6

    def test_led_can_switch_on_with_negative_duty_cycle(self, led_fixture):
        led_fixture.switch_on(duty_cycle=-1.0)
        assert led_fixture.duty_cycle == 0

    def test_led_can_switch_on_with_overlimit_duty_cycle(self, led_fixture):
        led_fixture.switch_on(duty_cycle=101.0)
        assert led_fixture.duty_cycle == 1e6