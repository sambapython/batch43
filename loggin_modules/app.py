import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="applog.txt",
                    format="%(asctime)s=>%(levelname)s==>%(message)s")
print "program started"
logging.info("program started")
logging.info("Taking an input from the user")
a=raw_input("Enter a value:")
b=raw_input("enter b value:")
logging.info("User input sucessfully taken")
print "a=%s, b=%s"%(a,b)
logging.debug("a=%s, b=%s"%(a,b))
try:
    logging.info("Converting a and b values to float")
    a=float(a)
    logging.info("a value conversion complted")
    b=float(b)
    logging.info("b value conversion complted")
    print "After conversion: a=%s, b=%s"%(a,b)
    logging.debug("After conversion: a=%s, b=%s"%(a,b))
    logging.info("calculating the result")
    res=a/b
    print "res=%s"%(res)
    logging.debug("RES=%s"%res)
except ValueError as err:
    logging.error(err)
    print "erroe:",err
    print "Enter only digits"
except ZeroDivisionError as err:
    logging.error(err)
    print "error:",err
    print "enter b!=0"
except Exception as err:
    logging.error(err)
    print "error:", err
    print "something went wrong"
else:
    print "else block"
finally:
    print "FINALLY BLOCK"
logging.info("operation completed successfully!!")
print "main block statements"
print "other statements in progrm"
print "program ended"