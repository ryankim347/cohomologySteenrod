from math import *

# index is any integer greater than log_2(n)
def recursePartitionPowerTwos(n,index):
	if index == 0:
		return 1
	count = 0
	for i in range (int(n/(2**index))+1):
		count = count + recursePartitionPowerTwos(n-i*(2**index),index-1)
	return count

# index is any integer greater than log_2(n)
def recurseSteenrod(n,index):
	if index == 1:
		return 1
	count = 0
	for i in range (int(n/(2**index-1)+1)):
		count = count + recurseSteenrod(n-i*(2**index-1),index-1)
	return count
  
# for each i, prints i, then number of solutions to $\sum_{j=0}^\infty a_j\cdot 2^j=i$, then number of solutions to $\sum_{j=1}^\infty a_j\cdot (2^j-1)=i$
for i in range (1,400):
	print(i,recursePartitionPowerTwos(i,9), recurseSteenrod(i,9))
