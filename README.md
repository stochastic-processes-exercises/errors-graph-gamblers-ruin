# Gamblers ruin plots with errors

The previous exercise showed you how to plot a dependent variable as a function of an independent variable.  There was one important factor that was left out in the previous exercise, however.  __The depedent variable in the plot that we drew is a random variable as such we need to provide some confidence interval around the estimate of this quantity that we have extracted via simulation.__  A confidence limit of this type is almost always drawn around dependent variables in graphs as there are almost always control variables that it is not possible to control in the experiment. These uncontrolled variables effect on the outcome of the experiment and thus introduce some randomness to the final value that is extracted.  

__In this exercise I would like you draw another of these graphs of a dependent variable as a function of a independent variable.__  This time, however, I want you to also use what you have learned elsewhere to calculate and plot suitable error bars on each of your estimates of the dependent variable.  The dependent variable will be the probability of ruin that you computed in the previous exercise.  Once again you should simulate the gamblers ruin problem stop the walk if the walker arrives in state `n=10`.  `n` will thus be one of your control variables.  The second control variable will be the start point which will be set as `s=5`.  The independent variable in your siulations is the probability of winning each game, `p`.  You should consider `p` values of 0.3, 0.4, 0.5 and 0.7.  
For each of these values of `p` you should estimate the probablity of ruin by simulating 200 random walks and calculating a mean.  Notice that you will also need to calculate a sample variance from these 200 random variables as you will need to calculate the error bar for a 90% confidence limit.

I have written the following plot commands in the `main.py` for you:

````
plt.errorbar( x, y, yerr=error, fmt='ko' )
plt.xlabel("Probability of winning each game")
plt.ylabel("Probability of ruin")
plt.savefig("graph.png")
````

Notice that you need to set the elements of the NumPy array called `error` equal to the width of the 90% confidence limit in order to pass the test.  This variable needs to be present and set in order to pass the tests as I check for its existence.

Notice, furthermore, that when you complete this exercise for real you can extend out the range of values you investigate.  I kept the range artifically low here so as to make the calculation less expensive.
