"""
Author Robert Munnoch
Taken info from https://docs.python.org/3/library/logging.handlers.html#sysloghandler
"""

import logging
import logging.handlers
import socket

my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(
    address = ('10.20.30.30',5514),
    socktype=socket.SOCK_DGRAM
)

my_logger.addHandler(handler)

my_logger.debug('debugging message')
my_logger.info('info message')
my_logger.warning('warning message')
my_logger.error('error message')
my_logger.critical('critical message')