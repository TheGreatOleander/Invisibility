import numpy as np
from .base import Adversary

class LocalAdversary(Adversary):
    def correlate(self, entry, exit):
        return np.corrcoef(entry[:len(entry)//2], exit[:len(exit)//2])[0,1]
