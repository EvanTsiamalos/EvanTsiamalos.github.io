import numpy as np
import matplotlib.pyplot as plt



def f(x):
	return np.sin(x)
	
	
def integralCalculation(g, c,d):		## Aproximates the integral using Simson's method
	return ((d-c)/6)*(g(c) + 4*g(0.5*(c+d)) + g(d))					
	


def aproximationCalculator(f,a,b,J):		## Calculates a step function ystar that is the optimal aproximation for f
	x = np.linspace(a,b,J+1)
	ystar = np.ones(J+1)
	
	h = (b-a)/J
	
	
	for k in range(1,J+1):
		ystar[k] = (1/h)*integralCalculation(f,x[k-1], x[k])
	ystar[0] = ystar[1]
	return x,ystar	
	
	






############## 

a = 0					## Interval [a,b]
b = 2*np.pi						 

#J= 10					## Number of points of partition
print('Give number J of points for the partition. J > 2') 
J= int(input('J = '))			
								
x = np.linspace(a,b,200)		
y = f(x)

xdiam , ystar = aproximationCalculator(f,a,b,J)			## Calculate the aproximation by step functions


plt.plot(x,y)
plt.step(xdiam,ystar,where='pre')


plt.show()

