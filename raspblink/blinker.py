__all__ = ["blink"]

from .waveform import generate_waveform
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import time

import pigpio

LED = 18

pi = pigpio.pi()
if not pi.connected:
    exit()


def blink(period: float = 1.00, n: int = 1) -> None:
    amp_values = generate_waveform()
    delay = period / 100

    for i in range(1, n + 1):
        logger.debug(f"iter: {i}...")
        start = time.perf_counter()
        for amp in amp_values:
            pi.hardware_PWM(LED, 100, amp)
            time.sleep(delay)
        logger.debug(f"period: {(time.perf_counter() - start) * 1000:+.3f}ms")
