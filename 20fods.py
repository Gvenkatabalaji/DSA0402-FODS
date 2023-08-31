import numpy as np
from scipy.stats import ttest_ind
design_A_conversion_rates = [13, 11, 10, 14, 12, 11, 9, 13, 10, 12]
design_B_conversion_rates = [14, 12, 9, 11, 13, 14, 8, 10, 11, 12]
mean_A = np.mean(design_A_conversion_rates)
mean_B = np.mean(design_B_conversion_rates)
std_A = np.std(design_A_conversion_rates,ddof=1)
std_B = np.std(design_B_conversion_rates,ddof=1)
n_A = len(design_A_conversion_rates)
n_B = len(design_B_conversion_rates)
t_stat, p_value = ttest_ind(design_A_conversion_rates, design_B_conversion_rates)
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and B.")