import logging
import pigpio

logger = logging.getLogger(__name__)


class PowerButton:
    def __init__(self):
        self._pi = pigpio.pi()
        if not self._pi.connected:
            exit()

    def switch_on(self):
        self._pi.hardware_PWM(18, 100, int(1e6))

    def switch_off(self):
        self._pi.hardware_PWM(18, 100, 0)
