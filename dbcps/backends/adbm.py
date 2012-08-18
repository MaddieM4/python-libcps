from dbcps.dbh import DBH
import anydbm
import os

print anydbm

class ADBM(DBH):
    '''
    Uses the anydbm module to store data to disc.

    >>> from dbcps import storage
    >>> from tempfile import mkstemp
    >>> fname = mkstemp()[1]
    >>> backend = ('adbm', fname, ['rotate', -91])
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

    def __init__(self, path, encryptor, handle='anydbm', filemode='c'):
        DBH.__init__(self, handle, encryptor)
        filesize = os.stat(path).st_size
        if filesize == 0:
            os.remove(path)
        self.db = anydbm.open(path, filemode)

    def get(self, k):
        return self.db[k]

    def set(self, k, i):
        self.db[k] = i

    def delete(self, k):
        del self.db[k]

    def contains(self, k):
        return k in self.db

dbh_class = ADBM
