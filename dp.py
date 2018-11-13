# Dynamic programming implementation for finding number of solutions to $\sum_{i=0}^\infty a_i\cdot 2^i=n$ and $\sum_{i=1}^\infty a_i\cdot (2^i-1)=n$
from math import *

# finds number of solutions to $\sum_{i=0}^\infty a_i\cdot 2^i=n$
def dpPartitionPowerTwos(n):
	dp = [[0 for a in range(ceil(log(n)/log(2))+1)] for b in range(n+1)]
	for i in range (n+1):
		for j in range (ceil(log(n)/log(2))+1):
			if j==0:
				dp[i][j] = 1
			else:
				count = 0
				for k in range(ceil(i/(2**j))):
					count = count + dp[i-k*(2**j)][j-1]
				dp[i][j] = count
	return dp[n][ceil(log(n)/log(2))]

def dpSteenrodHelper(n):
	dp = [[0 for a in range(ceil(log(n)/log(2)))] for b in range(n+1)]
	for i in range (n+1):
		for j in range (ceil(log(n)/log(2))):
			if j==0:
				dp[i][j] = 1
			else:
				count = 0
				for k in range(ceil(i/(2**(j+1)-1))):
					count = count + dp[i-k*(2**(j+1)-1)][j-1]
				dp[i][j] = count
	return dp[n][ceil(log(n)/log(2))-1]

# finds number of solutions to $\sum_{i=1}^\infty a_i\cdot (2^i-1)=n$
def dpSteenrod(n):
   return dpSteenrodHelper(n+1)

# for each i, prints i, and number of solutions to both equations
for i in range (1,400):
	print(i,dpPartitionPowerTwos(i), dpSteenrod(i))
