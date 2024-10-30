
import logging
import sys

logger = logging.getLogger('stripe')

__all__ = ['utf8']


def utf8(value):
    if isinstance(value, str) and sys.version_info < (3, 0):
        return value.encode('utf-8')
    elif isinstance(value, bytes):
        return value.decode('utf-8')
    return value
