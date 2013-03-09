import ejtp.crypto
from dbcps.filters.core import Filter

class CryptoFilter(Filter):
    def __init__(self, target=None, origin=None, encryptor=None):
        Filter.__init__(self, target, origin)
        self.encryptor = encryptor

    @property
    def encryptor(self):
        return self.attributes['encryptor']

    @encryptor.setter
    def encryptor(self, encryptor):
        self.attributes['encryptor'] = ejtp.crypto.make(encryptor)

    def __setitem__(self, k, v):
        k = self.encryptor.encrypt(k)
        v = self.encryptor.encrypt(v)
        self.target[k] = v

    def __getitem__(self, k):
        k = self.encryptor.encrypt(k)
        v = self.target[k]
        return self.encryptor.decrypt(v)

    def __delitem__(self, k):
        k = self.encryptor.encrypt(k)
        del self.target[k]
