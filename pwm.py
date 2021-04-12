#!/usr/bin/env python3

# def profile(func):
#     from functools import wraps

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         from line_profiler import LineProfiler

#         prof = LineProfiler()
#         try:
#             return prof(func)(*args, **kwargs)
#         finally:
#             prof.print_stats()

#     return wrapper

import pigpio
import time
import numpy as np
import matplotlib.pyplot as plt

LED = 18

pi = pigpio.pi()
if not pi.connected:
    exit()


def generate_waveform(plot: bool = False):
    time_vals = np.arange(0, 2 * np.pi, np.pi / 50)  # 100 values
    waveform = np.cos(time_vals) + 1.1
    amp_values = 1e6 * waveform / np.max(waveform)
    amp_values = amp_values.astype(int)  # int are smaller
    if plot:
        fig = plt.figure()
        plt.plot(time_vals, amp_values, "-")
        fig.savefig("waveform.png")
    return amp_values


print("generating waveform")
waveform = generate_waveform()
print("generated waveform")

for _x in range(1):
    for amp in waveform:
        # print(f"{amp:.2f}")
        pi.hardware_PWM(LED, 100, amp)  # 800Hz 25% dutycycle
        # pi.set_PWM_dutycycle(LED, 50)  # PWM off
        time.sleep(0.065)
