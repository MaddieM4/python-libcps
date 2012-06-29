from dbcps.dbh import DBH

class RAMDict(DBH):
    '''
    "Dummy" class for storing all data in memory in a dict.
    '''

    def __init__(self, encryptor):
        DBH.__init__(self, 'ramdict', encryptor)
        self._data = {}

    def get(self, k):
        return self._data[k]

    def set(self, k, i):
        self._data[k] = i

    def delete(self, k):
        del self._data[k]

dbh_class = RAMDict
