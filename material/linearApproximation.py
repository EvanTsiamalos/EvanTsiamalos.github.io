import numpy as np
import matplotlib.pyplot as plt



def f(x):
	return np.sin(x)
	

##############

left = 0								## We work in a interval [left , right]
right = 2*np.pi

print('Give number J of points for the partition, J > 2') 
J= int(input('J = '))									## Number of points of partition
h = (right - left)/J

d = (2*h/3)*np.ones(J + 1)						## Construction of matrix A of the linear System
d[0] = h/3
d[J] = h/3
e = (h/6) * np.ones(J)
A = np.diag(d,0) + np.diag(e,-1) + np.diag(e,1)



######
xdiam = np.linspace(left,right,J+1)
b = np.zeros(J + 1)

for i in range(J+1):										## Construction of array b of the linear System
	if i == 0:
		first = f(xdiam[0])
		second = f(0.5*(xdiam[0] + xdiam[1]))*0.5
		third = 0
		b[0] = (h/6)*(first + 4*second + third)
	elif i == J:
		first = 0
		second = f(0.5*(xdiam[J -1 ] + xdiam[J]))*0.5
		third = f(xdiam[J])
		b[J] = (h/6)*(first + 4*second + third)	
	else:
		b[i] = (h/6)*(2*f(0.5*(xdiam[i-1] + xdiam[i])) + 2*f(xdiam[i]) + 2*f(0.5*(xdiam[i] + xdiam[i+1])))		



####

astar = np.linalg.solve(A,b)			## Solution of the linear System


#print(astar)


x = np.linspace(left, right,120)		## Function f
y = f(x)										
										
plt.plot(x,y,'-.',linewidth = 3)		## Aproximation
plt.plot(xdiam,astar,'-')

plt.show()









