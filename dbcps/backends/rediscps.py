import redis
from dbcps.dbh import DBH
from ejtp.util import py2and3

class Redis(DBH):
    '''
    Uses the redis module to store data to a key value store.

    >>> from dbcps import storage
    >>> backend = ('rediscps', ['rotate', -91])
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
    'pancakes'
    '''

    def __init__(self, encryptor, handle='rediscps', host='localhost', port=6379):
        DBH.__init__(self, handle, encryptor)
        self.db = redis.Redis(host, port)

    def get(self, k):
        return self.db[k]

    def set(self, k, i):
        self.db[k] = i

    def delete(self, k):
        del self.db[k] 

    def contains(self, k):
        return k in self.db

dbh_class = Redis
