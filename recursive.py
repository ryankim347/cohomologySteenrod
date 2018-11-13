# Recursive implementation for finding number of solutions to $\sum_{i=0}^\infty a_i\cdot 2^i=n$ and $\sum_{i=1}^\infty a_i\cdot (2^i-1)=n$
from math import *

# if index is any integer greater than log_2(n), finds number of solutions to $\sum_{i=0}^\infty a_i\cdot 2^i=n$
def recursePartitionPowerTwos(n,index):
	if index == 0:
		return 1
	count = 0
	for i in range (int(n/(2**index))+1):
		count = count + recursePartitionPowerTwos(n-i*(2**index),index-1)
	return count

# if index is any integer greater than log_2(n), finds number of solutions to $\sum_{i=1}^\infty a_i\cdot (2^i-1)=n$
def recurseSteenrod(n,index):
	if index == 1:
		return 1
	count = 0
	for i in range (int(n/(2**index-1)+1)):
		count = count + recurseSteenrod(n-i*(2**index-1),index-1)
	return count
  
# for each i, prints i, then number of solutions to both equations
for i in range (1,400):
	print(i,recursePartitionPowerTwos(i,9), recurseSteenrod(i,9))
