#Radial Basis Function
# gamma : a
#h(x) = w1*exp(a|x - x1|**2) + w2*exp(a|x - x2|**2)

import numpy as np
# input data
x = np.linspace(1, 5, 5)
y = np.sin(x)

# answer data
x_ = np.linspace(1, 5, 100)
y_ = np.sin(x_)

import matplotlib.pyplot as plt
plt.scatter(x,y,color='r', label='observed point')
plt.plot(x_,y_,'b--',alpha=0.5, label='actual function')
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

c = 10 # gamma

# AW = Y -> W = A^(-1)Y
# A
A = [[np.exp( (-c) * (j - i)**2 ) for i in x] for j in x]
Y = y # [i for i in y]

# inverse matrix A^(-1)
A_ = np.linalg.inv(A)
W = np.matmul(A_, Y)

# new data matrix M & prediction matrix N
M = [ [np.exp( (-c) * (j - i)**2 ) for i in x] for j in x_]

# N = MW
N = np.matmul(M, W)

plt.scatter(x,y,color='r', label='observed point')
plt.scatter(x_, N,color='k',s=3,marker='x', label='prediction')
plt.plot(x_,y_,'b--',alpha=0.5, label='actual function')
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('$\gamma$ (gamma) : {}'.format(c))
plt.show()
