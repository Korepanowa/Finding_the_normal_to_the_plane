import numpy as np


A = [(26, 63, 70), (25, 63, 70), (24, 63, 70), (23, 63, 30), (22, 63, 50), (21, 63, 20), (20, 63, 59), (22, 62, 47), (27, 63, 70)]
A = np.array(A)
leftbottom = np.array((0,238, 30))
distances = np.linalg.norm(A-leftbottom, axis=1)
min_index = np.argmin(distances)
print(f"the closest point is {A[min_index]}, at a distance of {distances[min_index]}")




