class AttackCostModel:

    def __init__(self, compute_unit=0.001, sample_unit=0.0001):
        self.compute_unit = compute_unit
        self.sample_unit = sample_unit

    def estimate(self, samples, corr):
        base = samples * (self.compute_unit + self.sample_unit)
        difficulty = 1 / max(abs(corr), 0.0001)
        return base * difficulty
