import numpy as np
from .base import Adversary

class GlobalPassiveAdversary(Adversary):
    def __init__(self, noise=0.01):
        self.noise = noise

    def correlate(self, entry, exit):
        e = entry + np.random.normal(0, self.noise, len(entry))
        x = exit + np.random.normal(0, self.noise, len(exit))
        return np.corrcoef(e, x)[0,1]
