def sum_of_squares(max):
	result=0
	for number in range(max+1):
		result+=number**2
	return result
	
def sum_of_nth_squares(max):
	result=0
	for number in range(max+1):
		result+=number
	return result**2

	
a=sum_of_nth_squares(100)
b=sum_of_squares(100)
print (a-b)