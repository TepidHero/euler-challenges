def isPalindrome(a):
	for x,y in zip(a[:],a[::-1]):
		if x!=y:
			return False
	return True
	
works=0
for x in range(100,10,-1):
	for y in range(100,10,-1):
		if isPalindrome(x*y):
			works=(x*y)
			break
print (works)