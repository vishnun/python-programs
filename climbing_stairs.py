# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer. 

def climb_recursively(i, mem):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	elif i == 2:
		return 2
	elif mem[i] > 0:
		return mem[i]
	mem[i] = climb_recursively(i-1, mem) + climb_recursively(i-2, mem)
	return mem[i]

def climb(n):
	mem = (n+1)*[0]
	return climb_recursively(n, mem)

def climb_i(n):
	if n < 1:
		return 0
	res = [0] * n*2
	res[0] = 0
	res[1] = 1
	if n < 2:
		return res[n]
	res[2] = 2
	for i in range(3,n+1):
		res[i] = res[i-1] + res[i-2]
	return res[n]