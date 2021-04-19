__all__ = ["sine_waveform", "cosine_waveform"]

# References:
# https://makersportal.com/blog/2020/3/27/simple-breathing-led-in-arduino#:~:text=A%20breathing%20LED%20is%20a,of%20functionality%20to%20some%20degree.&text=Each%20function%20uses%20a%20loop,of%20a%20'breathing'%20LED.
# https://realpython.com/fast-flexible-pandas/

import logging
import time

logger = logging.getLogger(__name__)

start = time.time()
import numpy as np

t1 = time.time()
logger.debug(f"Imported numpy. Elapsed: {(t1 - start) * 1000:+.3f}ms")

t2 = time.time()
logger.debug(f"Imported typing. Elapsed: {(t2 - t1) * 1000:+.3f}ms")


def cosine_waveform(
    vertex: float = 0.3, inverse: bool = False, plot: bool = False
) -> np.ndarray:
    x = np.arange(0, 2 * np.pi, np.pi / 50)  # 100 values
    if inverse:
        waveform = -np.cos(x) + (1.0 + vertex)
    else:
        waveform = np.cos(x) + (1.0 + vertex)
    y = 1e6 * waveform / np.max(waveform)
    y = y.astype(int)  # int are smaller
    if plot:
        import matplotlib.pyplot as plt

        font = {
            "family": "serif",
            "color": "black",
            "weight": "normal",
            "size": 16,
        }
        fig = plt.figure()
        plt.title("Cosine Waveform for LED pulse", fontdict=font)
        plt.plot(x, y, "-")
        fig.savefig("waveform.png")
    return y


def sine_waveform(vertex: float = 0.3, plot: bool = False) -> np.ndarray:
    x = np.arange(0, 2 * np.pi, np.pi / 50)  # 100 values
    waveform = np.sin(x) + (1.0 + vertex)
    y = 1e6 * waveform / np.max(waveform)
    y = y.astype(int)  # int are smaller
    if plot:
        import matplotlib.pyplot as plt

        font = {
            "family": "serif",
            "color": "black",
            "weight": "normal",
            "size": 16,
        }
        fig = plt.figure()
        plt.title("Sine Waveform for LED pulse", fontdict=font)
        plt.plot(x, y, "-")
        fig.savefig("sine.png")
    return y