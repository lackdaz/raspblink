import logging
from typing_extensions import Literal
import pigpio
from .base_classes import BasePWM

logger = logging.getLogger(__name__)


class Pwm(BasePWM):
    frequency: int = 100

    def __init__(self, led_pin: Literal[12, 13, 18, 19] = 18):
        self._pi = pigpio.pi()
        if not self._pi.connected:
            raise Exception("Did you forget to run pigiod?")
            exit()
        self.led_pin = led_pin

    def switch_on(self, duty_cycle: float = 100.0):
        if duty_cycle < 0:
            duty_cycle = 0
        elif duty_cycle > 100.0:
            duty_cycle = 100.0
        duty_cycle *= 1e6 / 100
        self.duty_cycle = duty_cycle
        self._pi.hardware_PWM(self.led_pin, Pwm.frequency, int(duty_cycle))

    def switch_off(self):
        self.duty_cycle = 0
        self._pi.hardware_PWM(self.led_pin, Pwm.frequency, 0)
