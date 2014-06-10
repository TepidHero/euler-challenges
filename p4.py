def isPalindrome(a):
	number=str(a)
	length=len(number)
	if length==5:
		if number[0]==number[4]:
			if number[1]==[3]:
				return True
			else:
				return False
		else:
			return False
	else:
		if number[0]==number[5]:
			if number[1]==number[4]:
				if number[2]==number[3]:
					return True
				else:
					return False
			else:
				return False
		else:
			return False
works=[]
for x in range(1000,100,-1):
	for y in range(1000,100,-1):
		if isPalindrome(x*y):
			works.append(x*y)
print (max(works))