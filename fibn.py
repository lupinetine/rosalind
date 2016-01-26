def fibn(n, k):
	result = list()
	for x in range(1,n+1):
		if (x==1) or (x==2):
			result.append(1)
		else:
			#tmp = result[-2]*k + result[-1]
			
			result.append(result[-2]*k + result[-1])
	
	return result

print fibn(32, 2)