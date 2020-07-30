import logging


logger = logging.getLogger(__name__)

def func_a():
    logger.debug('This message will not be logged because logging level for "mylib" is set to INFO')
    logger.info('logging from a')