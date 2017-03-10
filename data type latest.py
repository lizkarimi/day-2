def data_type(n):
	if type(n)==int:
		if n>100:
			return n,"more than 100"
		elif n<100:
			return n,"less than 100"	
		else:
			return n,"equal to 100"
	elif type(n) == str:
		return len(n)
	elif n==None:
		return "no value"
	elif type(n)==bool:
		return n
	elif type(n)==list:
		try:
			return n[2]
		except Exception as e:
			return None
if __name__ == '__main__':
	print(data_type(None))