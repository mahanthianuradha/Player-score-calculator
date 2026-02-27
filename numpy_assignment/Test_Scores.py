import numpy as np
scores=np.array([85,90,78,92,88,76,95,82,89,91,87,84])
print(f"Shape:{scores.shape}")
print(f"Total elements:{scores.size}")
print(f"Highest score:{np.max(scores)}")
print(f"Lowest score:{np.min(scores)}")
print(f"Range:{max(scores)-min(scores)}")
