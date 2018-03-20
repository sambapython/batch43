import logging
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.WARN)
logging.basicConfig(level=logging.DEBUG,
					filename="log.txt",
					format="%(asctime)s=>%(levelname)s==>%(message)s")

logging.error("ERROR MESSAGE")
logging.debug("DEBUG MESSAGE")
logging.info("INFO MESSAGE")
logging.warn("WARNING MESSAGE")
