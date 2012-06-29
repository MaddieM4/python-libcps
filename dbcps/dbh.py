from ejtp.util import crypto

class DBH(object):
    '''
    Base class for all Database Handlers.
    '''
    def __init__(self, handle, encryptor):
        self.handle = handle
        self.encryptor = crypto.make(encryptor)

    # Subclass overrides

    def get(self, k):
        raise NotImplementedError('Backends must implement self,get(k)')

    def set(self, k, i):
        raise NotImplementedError('Backends must implement self,set(k, i)')

    def delete(self, k):
        raise NotImplementedError('Backends must implement self,delete(k)')

    # Interface/utility

    def __getitem__(self, k):
        k = self.encrypt(k)
        return self.decrypt(self.get(k))

    def __setitem__(self, k, i):
        k = self.encrypt(k)
        i = self.encrypt(i)
        self.set(k, i)

    def __delitem__(self, k):
        k = self.encrypt(k)
        self.delete(k)

    def encrypt(self, plaintext):
        return self.encryptor.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self.encryptor.decrypt(ciphertext)

def make_dbh(dbh_type, *args):
    dbh_module = __import__('dbcps.backends.'+dbh_type, fromlist=[''])
    print "Imported module for dbh_type %s: %r" % (dbh_type, dbh_module.__name__)
    return dbh_module.dbh_class(*args)
