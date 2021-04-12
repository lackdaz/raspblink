__all__ = ["generate_waveform"]

import logging
import time

logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

start = time.time()
import numpy as np

t1 = time.time()
logger.debug(f"Imported numpy. Elapsed: {(t1 - start) * 1000:+.3f}ms")
import numpy.typing as npt

t2 = time.time()
logger.debug(f"Imported typing. Elapsed: {(t2 - t1) * 1000:+.3f}ms")


def generate_waveform(plot: bool = False) -> np.ndarray:
    time_vals = np.arange(0, 2 * np.pi, np.pi / 50)  # 100 values
    waveform = np.cos(time_vals) + 1.0
    amp_values = 1e6 * waveform / np.max(waveform)
    amp_values = amp_values.astype(int)  # int are smaller
    if plot:
        import matplotlib.pyplot as plt

        fig = plt.figure()
        plt.plot(time_vals, amp_values, "-")
        fig.savefig("waveform.png")
    return amp_values