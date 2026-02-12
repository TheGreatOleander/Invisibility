import numpy as np
from .base import Adversary

class RegionalAdversary(Adversary):
    def correlate(self, entry, exit):
        return np.corrcoef(entry, exit)[0,1] * 0.8
