import logging
# logging.debug('The debug message is displaying')
# logging.info('The info message is displaying')
# logging.warning('The warning message is displaying')
# logging.error('The error message is displaying')
# logging.critical('The critical message is displaying')

logging.basicConfig(filename = 'msg.log',filemode = 'w',format = '%(name)s - %(levelname)s - %(message)s') 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.warning('this will get logged in to a file')
logger.error('The error message is displaying')
logger.critical('The critical message is displaying')
logger.debug('The debug message is displaying')