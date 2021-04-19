__all__ = ["Flash"]

from time import sleep
import RPi.GPIO as GPIO

import sys
from threading import Thread

from ..board import *

from typing import List, Optional
from .pwm import PWM

if sys.version_info.major < 3:
    print("You need to run this on Python 3")
    sys.exit(-1)


class Flash(PWM):
    __slots__ = ["task"]

    def __new__(cls, pin: str, *args, **kwargs):
        if pin in flash_pins:
            return super().__new__(cls, pin)
        else:
            raise KeyError(f"Not a Flash assigned pin. Choose any of {flash_pins}")

    def __init__(self, pin: str, *args, **kwargs):
        super().__init__(pin, *args, **kwargs)
        self.task: Optional[Thread] = None

    def flash_routine(self, exposure: float, delay: float, duty_cycle: float):
        """[summary]
        Args:
            exposure (float): Flash exposure (ms)
            delay (float): Delay before flash (ms)
            duty_cycle (float): Duty cycle in %. Defaults to 100.
        """
        sleep(delay / 1000.0)  # ms
        self.start(duty_cycle)
        sleep(exposure / 1000.0)  # ms
        self.stop()
        self.task = None

    def exec(self, exposure: float, delay: float, duty_cycle: float = 100.0):
        """[summary]
        Args:
            exposure (float): Flash exposure in ms
            delay (float): Delay before flash (ms)
            duty_cycle (float, optional): Duty cycle in %. Defaults to 100.
        """
        if self.task:
            return
        print(f"exposure: {exposure}ms, delay: {delay}ms, duty_cycle: {duty_cycle}%")
        self.task = Thread(
            target=self.flash_routine, args=[exposure, delay, duty_cycle]
        )
        self.task.start()
