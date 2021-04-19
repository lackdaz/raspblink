# from .blink import *
from .power_button import *
from .pwm import *
from .led import *
from .generator import *

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)