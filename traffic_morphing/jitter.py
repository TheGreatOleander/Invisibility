import numpy as np

def apply_jitter(timestamps, max_delay):
    return timestamps + np.random.uniform(0, max_delay, len(timestamps))
