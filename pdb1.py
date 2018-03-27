"""
to xeplanin pdb module
"""
a=10
b=20
c=a+b
print "a=%s,b=%s,c=%s"%(a,b,c)
def fun(c1,c2):
	"""
	expecting c1,c2 should int type
	For multiplication purpose
	"""
	try:
		print "c1=%s, c2=%s"%(c1,c2)
		print "this is function"
		res=c1*c2
		return res
	except Exception as err:
		print err
print "some st6atements"
import pdb;pdb.set_trace()
fun(10,20)
for i in [-3,-2,-1,0,1,2,3]:
	if i!=0:
		res1=10/i
		print res1
print "other statements in program"
print "program ended"