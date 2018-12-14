# https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial
import logging
import sys


def get_logger(name):
    """
    https://stackoverflow.com/questions/28330317/print-timestamp-for-logging-in-python
    https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial
    https://docs.python.org/3.6/howto/logging.html#logging-to-a-file
    :param name: logger name
    :return: a configured logger
    """
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # add one or more handlers

    # log to file
    handler = logging.FileHandler('./data/output/fib.log', mode='w')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # log to terminal stdout
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

    return logger
