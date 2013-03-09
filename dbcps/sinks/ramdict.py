from dbcps.sinks.core import Sink

class RAMDict(Sink):
    '''
    "Dummy" class for storing all data in memory in a dict.

    >>> s = RAMDict()
    >>> s['hello'] = 'world'
    >>> s['hello']
    'world'
    >>> 'hello' in s
    True
    >>> 'hell' in s
    False
    >>> del s['hello']
    >>> 'hello' in s
    False
    >>> s['blueberry'] = 'pancakes'
    >>> del s
    >>> s = RAMDict()
    >>> s['blueberry']
    Traceback (most recent call last):
    ...
    KeyError: 'blueberry'
    '''

    def __init__(self, origin=None):
        Sink.__init__(self, origin)
        self.backend = {}
