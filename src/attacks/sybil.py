import numpy as np

class SybilAttack:
    def __init__(self, num_sybil, scale=10):
        self.num_sybil = num_sybil
        self.scale = scale

    def generate(self, honest_updates):
        base = np.mean(list(honest_updates.values()), axis=0)
        return {f"sybil_{i}": base * self.scale for i in range(self.num_sybil)}
