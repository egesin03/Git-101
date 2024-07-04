import numpy as np
import matplotlib.pyplot as plt

# Define x values for plotting (avoiding zero)
x_values = np.linspace(0.1, 10, 400)
ln_x_values = np.log(x_values)
ln_P_greater_x = -x_values ** 2  # Since P[X > x] = exp(-x^2) for beta=2, lambda=1

# Plot ln(P[X > x]) vs ln(x)
plt.figure(figsize=(10, 6))
plt.plot(ln_x_values, ln_P_greater_x, marker='o', linestyle='-', color='blue')
plt.title(r'Plot of $\ln P[X > x]$ vs $\ln x$')
plt.xlabel(r'$\ln x$')
plt.ylabel(r'$\ln P[X > x]$')
plt.grid(True)
plt.show()