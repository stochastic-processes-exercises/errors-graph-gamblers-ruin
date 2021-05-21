import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Your code to simulate the walker and to calculate the errors goes here


plt.errorbar( x, y, yerr=error, fmt='ko' )
plt.xlabel("Probability of winning each game")
plt.ylabel("Probability of ruin")
plt.savefig("graph.png")
