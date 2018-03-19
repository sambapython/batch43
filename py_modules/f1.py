
def fun():
	print "this is fun in f1 modified after pyc"

if __name__ == "__main__":
	def fun1():
		print "this is fun1 in f1"
	print "name:",__name__
	print "this is f1"
	fun()
	fun1()
	print "other statements in progrm"
	print "program ended"

