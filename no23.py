import numpy as np

plus_hk = np.array([-4, 6, -2])
minus_hk = np.array([6, -3, 7])

h = (plus_hk + minus_hk) / 2
k = (plus_hk - minus_hk) / 2

norm_h_plus_k_squared = np.sum(plus_hk**2)
norm_h_minus_k_squared = np.sum(minus_hk**2)

print("|h + k|^2 =", norm_h_plus_k_squared)
print("|h - k|^2 =", norm_h_minus_k_squared)

dot_hk = (norm_h_plus_k_squared - norm_h_minus_k_squared) / 4

print("h . k =", dot_hk)
