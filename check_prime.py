# To test use this list of prime numbers: http://www.bigprimes.net/archive/prime/
import random

def is_prime(num):
	rand_nums = [random.randint(2,num-1) for i in range(num/2)]
	rand_nums = list(set(rand_nums))
	for a in rand_nums:
		if (pow(a, num-1) % num) != 1:
			return False
	return True