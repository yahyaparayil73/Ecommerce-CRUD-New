import logging

logging.basicConfig(filename = 'sample.log',filemode = 'w',format = '%(asctime)s %(levelname)s - %(message)s') 

a = 10
b = 0
try:
    c = a/b
except Exception as e : 
    logging.error('Exception occured',exc_info = True)
    