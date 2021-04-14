__all__ = ["blink"]

# References
# https://medium.com/@rxseger/pulse-width-modulation-using-pwm-to-build-a-breathing-nightlight-and-alarm-6f3ff5682afc

from .waveform import generate_waveform
import logging
from typing_extensions import Literal

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import time

import pigpio


class Blinker(object):
    def __init__(self, led_pin: Literal[14, 18] = 18):
        self.pi = pigpio.pi()
        self._led_pin = led_pin
        if not self.pi.connected:
            raise Exception("Is pigpiod running?")

    @property
    def led_pin(self):
        return self._led_pin

    @property.setter
    def led_pin(self, led_pin: Literal[14, 18]):
        if led_pin not in [12, 13, 18, 19]:
            raise Exception("boo!")
        return self._led_pin

    def blink(self,                  af                                                                                                                                                                          zsf                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            v          d xperiod: float = 1.00, n: int = 1) -> None:
        assert 0.1 < period < 10, "period must be with 0.1 - 10s"
        amp_values = generate_waveform()
        delay = period / 100

        for i in range(1, n + 1):
            logger.debug(f"iter: {i}...")
            start = time.perf_counter()
            for amp in amp_values:
                pi.hardware_PWM(LED, 100, amp)
                time.sleep(delay)
            logger.debug(f"period: {(time.perf_counter() - start) * 1000:+.3f}ms")
