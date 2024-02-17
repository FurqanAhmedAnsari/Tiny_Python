# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

# Create a data frame with the observed frequencies
df = pd.DataFrame({"IA.Time": [0,1,2,3,4,5,6,8,13,17,18,19,20,23,24,26,28,30,32,
                               33,34,36,43,47,48,50,54,55,56,57,65],
                   "Obs.Freq": [11,18,18,28,18,26,16,18,10,
                                17,
                                20,
                                8,
                                26,
                                44,
                                28,
                                36,
                                19,
                                18,
                                16,
                                10,
                                8,
                                8,
                                18,
                                9,
                                19,
                                8,
                                8,
                                10,
                                9,
                                8,
                                1]})

# Plot a histogram of the observed frequencies
plt.hist(df["Obs.Freq"], density=True , edgecolor="black")

# Estimate the scale parameter of the exponential distribution
scale = df["Obs.Freq"].mean()

# Plot an exponential distribution with the same scale parameter
x = np.linspace(0 , df["Obs.Freq"].max() , 100)
y = expon.pdf(x , scale=scale)
plt.plot(x , y , color="red")

# Show the plot
plt.show()
