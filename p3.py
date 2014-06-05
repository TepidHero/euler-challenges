#list factors of input
def big_factor(num):
	list=[]
	for i in range(1,num):
		if num%i==0:
			list.append(i)
	return list
	
def factor_list(list):
	result=[]
	for num in list:
		for small in range(1,num):
			if num%small==0:
				result.append(small)
	return result
	
print (big_factor(6857))