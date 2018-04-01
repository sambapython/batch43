import unittest
from app import fun
class AppTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "SETUP CLASS"
		print "login"
		cls.user="user1"

	@classmethod
	def tearDownClass(cls):
		print "TEARDOWN CLASS"
		print "logout from app"
		cls.user=None
	def setUp(self):
		print "SETUP"
		print "reserve a resource"
	def tearDown(self):
		print "TEAR DOWN"
		print "release a resource"

	def test_10_20(self):
		print "executing test1"
		
		print self.user
		act=fun(10,20)
		exp=30
		self.assertEqual(act,exp,"test_10_20 failed")
		

	def test_10_str1(self):
		print "executing test2"
		print self.user
		act=fun(10,"str1")
		exp=None
		self.assertEqual(act,exp,"test_10_str1 failed")
	def test_10_str2(self):
		print "executing test2"
		print self.user
		act=fun(10,"str2")
		exp=None
		self.assertEqual(act,exp,"test_10_str2 failed")
	def test_10_str3(self):
		print "executing test2"
		print self.user
		act=fun(10,"str3")
		exp=None
		self.assertEqual(act,exp,"test_10_str3 failed")
unittest.main()
#unittest.main() this is not required for notests