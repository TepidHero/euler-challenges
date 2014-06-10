def is_divisable(number):
	if number%20!=0:
		return False
	elif number%19!=0:
		return False
		  
	elif number%18!=0:
		return False
		  
	elif number%17!=0:
		return False
		  
	elif number%16!=0:
		return False
		  
	elif number%15!=0:
		return False
		  
	elif number%14!=0:
		return False
		  
	elif number%13!=0:
		return False
		  
	elif number%12!=0:
		return False
		  
	elif number%11!=0:
		return False
		  
	elif number%10!=0:
		return False
		  
	elif number%9!=0:
		return False
		  
	elif number%7!=0:
		return False
		  
	elif number%6!=0:
		return False
		  
	elif number%5!=0:
		return False
		  
	elif number%3!=0:
		return False
		  
	else:
		return True
		  
for i in range(1,100000000000000000,1):
	if is_divisable(i):
		print (i)
		break  