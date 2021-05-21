import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Your code to simulate the walker and to calculate the errors goes here
def random_walker(start, n, p) :
  while (start>0 and start<n ) :
     if np.random.uniform(0,1)<p : start=start+1
     else : start=start-1
  if start==0 : return 1
  else : return 0

def sample_mean(start,n,p,m) :
  S, S2 = 0, 0
  for i in range(m) :
      myvar = random_walker( start, n, p )
      S, S2 = S + myvar, S + myvar*myvar
  mean = S / m
  var = (m/(m-1))*( S2/m - mean*mean )
  eee = np.sqrt(var/m)*scipy.stats.norm.ppf(0.95)
  return mean, eee

x, y, error = np.linspace(0.1,0.9,9), np.zeros(9), np.zeros(9)
for i in range(1,10) : y[i-1], error[i-1] = sample_mean(5,10,i*0.1,200)

plt.errorbar( x, y, yerr=error, fmt='ko' )
plt.xlabel("Probability of winning each game")
plt.ylabel("Probability of ruin")
plt.savefig("graph.png")
