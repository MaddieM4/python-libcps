from dbcps.dbh import DBH

class RAMDict(DBH):
    '''
    "Dummy" class for storing all data in memory in a dict.

    >>> from dbcps import storage
    >>> backend = ('ramdict', ['rotate', 43])
    >>> s = storage.Storage([backend])
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
    >>> s = storage.Storage([backend])
    >>> s['blueberry']
    Traceback (most recent call last):
    ...
    KeyError: 'blueberry'
    '''

    def __init__(self, encryptor, handle='ramdict'):
        DBH.__init__(self, handle, encryptor)
        self._data = {}

    def get(self, k):
        return self._data[k]

    def set(self, k, i):
        self._data[k] = i

    def delete(self, k):
        del self._data[k]

    def contains(self, k):
        return k in self._data

dbh_class = RAMDict
