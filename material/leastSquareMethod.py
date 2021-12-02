import numpy as np
import matplotlib.pyplot as plt


'''
	Takes a String with the filename
	Returns the x and y arrays of data		
'''
def readData(filename):

    fh = open(filename,'r')
    L = fh.readlines()
    fh.close()
    M = []
    for i in range(len(L)):
        L[i] = L[i].strip()
        L[i] = L[i].split()
        
    x = []
    y = []
    for line in L:
        x.append(float(line[0]))
        y.append(float(line[1]))
    x = np.array(x)
    y = np.array(y)
    return x,y
			
'''
	Function that calculates the inner product of two aeeays
'''
def innerProd(x,y):

    return (x*y).sum()	
    
		
'''
	Function that calculates the base points z^l according to the base of the polynomials {1, t, t^2, ... , t^m}
	Returns an array z that contains the values of t^l on point x
	'''
def basePoints(x,l):

    return x**(l-1)
    

def polHorner(coef,x):
	m = len(coef)-1
	pk = coef[m]
	m -= 1
	while m>=0:
		pk = coef[m] + x*pk
		m-=1
	return pk
	
##################################3
filename = 'data.txt'
x,y = readData(filename)
					
K = x.shape[0]		## Number of points xi

m = int(input('Give degree of the polynomial: '))



### We are going to construct the matrix and the array b such that Aa = b
### We solve for a with the cholesky method


### Construction of b

b = np.array([innerProd(y,basePoints(x,l)) for l in range(1,m+2)])

### Construction of A

A = np.zeros((m+1,m+1))
for i in range(m+1):
    for j in range(m+1):
        A[i][j] = innerProd(basePoints(x,i+1),basePoints(x,j+1))

### Solve

G = np.linalg.cholesky(A)  ## The cholesky decomposition of A

a = np.linalg.solve(G.T,np.linalg.solve(G,b))





### Plot the points and the polynomial
plt.plot(x,y,'.')


xx = np.linspace(min(x),max(x),200)
pol = polHorner(a,xx)

plt.plot(xx,pol)

plt.show()
