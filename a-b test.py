import math

def estimated_parameters(N: int, n: int):
 p = n / N
 sigma = math.sqrt(p * (1 - p) / N)
 return p, sigma


def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
 p_A, sigma_A = estimated_parameters(N_A, n_A)
 p_B, sigma_B = estimated_parameters(N_B, n_B)
 return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

 z = a_b_test_statistic(1000, 200, 1000, 180) # -1.14

 two_sided_p_value(z) # 0.254

 z = a_b_test_statistic(1000, 200, 1000, 150) # -2.94
 two_sided_p_value(z) # 0.003