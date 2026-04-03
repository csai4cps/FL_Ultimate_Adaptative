import numpy as np

class AdaptiveUltimateAggregator:
    def aggregate(self, updates):
        return np.mean(list(updates.values()), axis=0)
