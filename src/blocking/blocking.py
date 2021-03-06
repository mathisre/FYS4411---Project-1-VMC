from numpy import log2, zeros, mean, var, sum, loadtxt, arange, array, cumsum, dot, transpose, diagonal, floor, trim_zeros, append
from numpy.linalg import inv
from time import time
from sys import argv

def block(x):
    # preliminaries
    n = len(x); d = int(log2(n)); s, gamma = zeros(d), zeros(d);
    mu = mean(x); t0 = time()

    # estimate the auto-covariance and variances 
    # for each blocking transformation
    for i in arange(0,d):
        n = len(x)
        # estimate autocovariance of x
        gamma[i] = (n)**(-1)*sum( (x[0:(n-1)]-mu)*(x[1:n]-mu) )
        # estimate variance of x
        s[i] = var(x)
        # perform blocking transformation
        x = 0.5*(x[0::2] + x[1::2])
   
    # generate the test observator M_k from the theorem
    M = (cumsum( ((gamma/s)**2*2**arange(1,d+1)[::-1])[::-1] )  )[::-1]

    # we need a list of magic numbers
    q =array([6.634897,9.210340, 11.344867, 13.276704, 15.086272, 16.811894, 18.475307, 20.090235, 21.665994, 23.209251, 24.724970, 26.216967, 27.688250, 29.141238, 30.577914, 31.999927, 33.408664, 34.805306, 36.190869, 37.566235, 38.932173, 40.289360, 41.638398, 42.979820, 44.314105, 45.641683, 46.962942, 48.278236, 49.587884, 50.892181])

    # use magic to determine when we should have stopped blocking
    for k in arange(0,d):
        if(M[k] < q[k]):
            break
    if(k >= d-1):
        print "Warning: Use more data"
    ans = s[k]/2**(d-k)
    print "Runtime: %g sec" % (time()-t0); print "Blocking Statistics :"
    print "average            iterations      std. error"
    print "%8g %20g %15g" % (mu, k, ans**.5)
    return ans

# input data must be a power of two
#x = loadtxt(argv[1])
#x = x[int(0.75*len(x)):len(x)]


v = loadtxt("/home/dsacco/Desktop/Data/new/Alpha_0.502100_dim_3_particles_100.dat")
  
print len(v)   
#v=v[0:512]

x1=v[len(v)-524288:len(v)]
#x1=v[len(v)-512:len(v)]
#x2=v[len(v)-262144:len(v)]
#x=v[len(v)-131072:len(v)]

#x1=x[len(x)-32768:len(x)]
#x2=x[len(x)-16384:len(x)]
#x=x[len(x)-65536:len(x)]

print len(x1)
import numpy as np
#x = np.asarray(x)
#x2 = np.asarray(x2)
x1 = np.asarray(x1)
print np.std(x)


ans1 = block(x1)
#ans2 = block(x2)
#ans = block(x)


