redislib = __import__("redis", {})
from dbcps.sinks.core import Sink

class Redis(Sink):
    '''
    Uses the redis module to store data to a key value store.

    >>> from __future__ import print_function
    >>> s = Redis()
    >>> s['hello'] = 'world'
    >>> print(s['hello'].decode())
    world
    >>> 'hello' in s
    True
    >>> 'hell' in s
    False
    >>> del s['hello']
    >>> 'hello' in s
    False
    >>> s['blueberry'] = 'pancakes'
    >>> del s
    >>> s = Redis()
    >>> print(s['blueberry'].decode())
    pancakes
    '''

    def __init__(self, origin=None, host='localhost', port=6379):
        Sink.__init__(self, origin)
        self.backend = redislib.Redis(host, port)
