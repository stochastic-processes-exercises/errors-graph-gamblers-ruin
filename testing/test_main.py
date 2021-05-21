try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot
           
from AutoFeedback.randomclass import randomvar
from AutoFeedback.plotclass import line
import unittest
from main import *

class errclass :
   def get_error(i) :
       from scipy.stats import norm
       return ( error[i] / norm.ppf(0.05) )**2

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        n, s = 10, 5
        x, e, var, bmin, bmax, isi  = [], [], [], [], [], []
        for s in range(1,10) : 
            x.append( s )
            rat = (1-s*0.1) / (s*0.1) 
            if( s==5 ) : prob = ( n - s ) / n
            else : prob = ( rat**s - rat**n ) / ( 1 - rat**n )
            e.append( prob )
            var.append( prob*(1-prob) / 200 )
            bmin.append(0)
            bmax.append(1)
            isi.append(False)

        val = randomvar( e, variance=var, vmin=bmin, vmax=bmax, isinteger=isi )
        line1=line( x, val )
        axislabels=["start point", "probability of ruin"]
        assert(check_plot([line1],explabels=axislabels,explegend=False,output=True))

    def test_errors(self) :
        inputs, variables = [], []
        for s in range(1,10) :
            rat = (1-s*0.1) / (s*0.1)
            if( s==5 ) : prob = ( n - s ) / n
            else : prob = ( rat**s - rat**n ) / ( 1 - rat**n )
            inputs.append((s,))
            myvar = randomvar( prob, dist="chi2", variance=prob*(1-prob)/200, isinteger=False)
            variables.append( myvar )
        assert( check_func("get_error", inputs, variables, modname=errclass ) )
