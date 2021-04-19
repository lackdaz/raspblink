import time
import logging
from .base_classes import BaseLED, Singleton
from .pwm import Pwm
from .thread import LEDThread
from .generator import cosine_waveform

logger = logging.getLogger(__name__)


class LED(BaseLED, Pwm, LEDThread):
    waveform = cosine_waveform(inverse=True)

    def __init__(self):
        super().__init__()
        self.duty_cycle: int = 0

    def slow_on(self, period: float):
        num_samples = len(LED.waveform) // 2  #  just take half
        samples = LED.waveform[:num_samples]
        delay = period / num_samples

        for amp in samples:
            self._pi.hardware_PWM(self.led_pin, 100, amp)
            time.sleep(delay)

    def slow_off(self, period: float):
        num_samples = len(LED.waveform) // 2  #  just take a quarter
        samples = LED.waveform[num_samples:]
        print(num_samples)
        delay = period / num_samples

        for amp in samples:
            self._pi.hardware_PWM(self.led_pin, 100, amp)
            time.sleep(delay)

    def pulse(self):
        while True:
            logger.debug(f"cairo!")
            time.sleep(5)

    def test_start(self, duration=5.0):
        self.start(self.pulse)

    def test_stop(self):
        self.stop(self.switch_off)