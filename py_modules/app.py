
#fun()
#import f1
#fun()
'''
import f1
f1.fun()
import sys
print sys.path
import f2
'''
'''
import sys
print sys.path
import f2
f2.fun()
import f1
f1.fun()
'''
'''
import sys
py2=sys.path[2]
cur=sys.path[0]
sys.path[2]=cur
sys.path[0]=py2
print sys.path
import f1
f1.fun()
'''
'''
import sys
print sys.path
sys.path.append("/home/khyaathi-python")
print sys.path
import f3
f3.fun()
'''
'''
import f1
f1.fun()
'''
#import module1
#from module1 import file1
'''
import module1
module1.file1.fun()
'''
'''
import module1
print module1.a
module1.file1.fun()
module1.file2.fun()
'''
'''
import module1
module1.file1.fun()
'''
'''
import f1
f1.fun()
'''
'''
import module1
module1.file1.fun()
'''
'''
from module1 import file1
file1.fun()
'''
'''
import module1
module1.file1.fun()
'''
'''
from module1 import file1
file1.fun()
'''
import f1
f1.fun()
f1.fun1()