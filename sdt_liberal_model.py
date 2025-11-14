import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 

#  SDT parameters 
D_PRIME = 1.0 
CRITERION = -0.5 
NOISE_MEAN = 0
STD_DEV = 1

# X-axis range for plotting
X_RANGE = np.linspace(-4, NOISE_MEAN + D_PRIME + 4, 300)

# Calculate the noise and signal distributions
noise_distribution = norm(NOISE_MEAN, STD_DEV)
signal_distribution = norm(NOISE_MEAN + D_PRIME, STD_DEV)

# Signal + Noise Mean 
SN_MEAN = NOISE_MEAN + D_PRIME 

# Calculate False Alarm and Hit Rates
FA_RATE = norm.sf(CRITERION, loc=NOISE_MEAN, scale=STD_DEV)
HIT_RATE = norm.sf(CRITERION, loc=SN_MEAN, scale=STD_DEV)

plt.figure(figsize=(10, 6))
plt.plot(X_RANGE, noise_distribution.pdf(X_RANGE), color = "blue",label='Noise Distribution')
plt.plot(X_RANGE, signal_distribution.pdf(X_RANGE), color = "red", label='Signal + Noise  Distribution')

plt.axvline(CRITERION, color='black', linestyle='--', label=f'Criterion (c = {CRITERION})')

# False Alarm Area (blue curve, right of criterion)
plt.fill_between(X_RANGE, noise_distribution.pdf(X_RANGE), where=(X_RANGE >= CRITERION), color='skyblue', alpha=0.4, hatch='//', label='False Alarm Rate')
#  Hit Area (red curve, right of criterion)
plt.fill_between(X_RANGE, signal_distribution.pdf(X_RANGE), where=(X_RANGE >= CRITERION), color='salmon', alpha=0.4, hatch='--', label='Hit Rate')

plt.text(CRITERION + 0.1, noise_distribution.pdf(X_RANGE)[X_RANGE >= CRITERION].max() * 0.5, 
         f'FA Rate: {FA_RATE:.2f}', color='blue', fontsize=10)
plt.text(CRITERION + 0.1, signal_distribution.pdf(X_RANGE)[X_RANGE >= CRITERION].max() * 0.7, 
         f'Hit Rate: {HIT_RATE:.2f}', color='red', fontsize=10)

# Plot settings
plt.title(f'Signal Detection Theory (SDT) Model: d\' = {D_PRIME}, c = {CRITERION}')
plt.xlabel('Internal Evidence Strength')
plt.ylabel('Probability Density (P(x))')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('sdt_liberal_d1_c_neg0_5_shaded.png')
plt.show()


print("SDT Cognitive Metrics")
print(f"Sensitivity (d'): {D_PRIME:.2f}")
print(f"Criterion (c): {CRITERION:.2f}")
print(f"False Alarm Rate (FA): {FA_RATE:.4f}")
print(f"Hit Rate (H): {HIT_RATE:.4f}")
