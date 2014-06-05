sum=0
def fibo(n):
	if n<2:
		return n
	return fibo(n-2)+fibo(n-1)
	
for i in range(35):
	if fibo(i)%2==0 and fibo(i)<4000000:
		sum+=fibo(i)
print (sum)