# https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial
import logging
import sys


def get_logger(name):
    """
    https://stackoverflow.com/questions/22807972/python-best-practice-in-terms-of-logging
    https://stackoverflow.com/questions/28330317/print-timestamp-for-logging-in-python
    https://docs.python.org/3/library/logging.html#formatter-objects
    https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial
    https://docs.python.org/3.6/howto/logging.html#logging-to-a-file
    :param name: logger name
    :return: a configured logger
    """
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(funcName)s line:%(lineno)s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # add one or more handlers

    # log to terminal stdout
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

    """
    comment out log to file.
    instead log to stream only.
    let program user decide if they want to pipe stream output to a file e.g.
        python3 fibonacci.py >> ../fib.log
        python3 -m unittest >> ../test.log
    references
    "logging in an application"
    https://docs.python-guide.org/writing/logging/
    https://12factor.net/logs
    """
    # log to file
    # mode 'a' append, not 'w' write
    # handler = logging.FileHandler('./data/output/fib.log', mode='a')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    return logger

