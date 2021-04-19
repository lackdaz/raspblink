class BaseLED:
    def __init__(pin):
        self._led_pin: int = pin
        self.led_state: bool = False

    @property
    def led_pin(self):
        return self._led_pin

    @property
    def led_state(self):
        return self.led_state

    @property.setter
    def led_state(self, state: bool):
        self.led_state = state

    def on(self):
        self.led_state = True
