import numpy as np

def run_mix_chain(messages, hops, delay_mean=1.0):
    for _ in range(hops):
        delays = np.random.exponential(delay_mean, len(messages))
        messages = np.random.permutation(messages + delays)
    return messages
