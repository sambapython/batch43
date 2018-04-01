def fun(a,b):
	"""
	expecting only integers or float for a,b
	params: a, int/float
			b, int/float
	return: summation, int/float
	"""
	try:
		return a+b
	except Exception as err:
		print err