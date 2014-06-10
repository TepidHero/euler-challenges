def is_triple(a,b,c):
	if a**2+b**2==c**2:
		return True
	elif a**2+c**2==b**2:
		return True
	elif a**2==b**2+c**2:
		return True
	else:
		return False
		
for a in range(1001):
	for b in range(1001):
		for c in range(1001):
			if is_triple(a,b,c):
				if a+b+c==1000:
					print (a*b*c)
					break