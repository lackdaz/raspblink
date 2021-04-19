__all__ = ["blink"]

import logging
import time
import pigpio
from . import generator

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


LED = 18

pi = pigpio.pi()
if not pi.connected:
    exit()


def blink(period: float = 1.00, n: int = 1) -> None:
    assert 0.1 <= period < 10.0, "period must be within 0.1 - 10.0s"
    amp_values = generator.sine_waveform()
    delay = period / 100

    for i in range(1, n + 1):
        logger.debug(f"iter: {i}...")
        start = time.perf_counter()
        for amp in amp_values:
            pi.hardware_PWM(LED, 100, amp)
            time.sleep(delay)
        logger.debug(f"period: {(time.perf_counter() - start) * 1000:+.3f}ms")
