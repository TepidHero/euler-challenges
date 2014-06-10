def is_prime(x):
	for smaller in range(2,x):
		if x%smaller==0:
			return False
		else:
			return True

primes=[]			
for i in range(2,1000000):
	if is_prime(i):
		primes.append(i)
	length=len(primes)
	

print (primes[10000])