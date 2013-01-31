from dbcps.dbh import make_dbh

class Storage(object):
    def __init__(self, backends=[]):
        self.handles = {}
        self.install(backends)

    def install(self, backends):
        for backend in backends:
            dbh = make_dbh(*backend)
            handle = dbh.handle
            self.handles[handle] = dbh

    def uninstall(self, handle):
        del self.handles[handle]

    def get_handle(self, key=''):
        handles = list(self.handles.keys())
        if len(handles):
            handles.sort()
            return handles[0]
        else:
            raise NoHandleError()

    def get_dbh(self, key=''):
        return self.handles[self.get_handle(key)]

    def __getitem__(self, k):
        if not isinstance(k, str):
            raise TypeError("Keys must be strings, got %r" % k)
        try:
            return self.get_dbh(k)[k]
        except KeyError:
            raise KeyError(k)

    def __setitem__(self, k, i):
        if not isinstance(k, str):
            raise TypeError("Keys must be strings, got %r" % k)
        if not isinstance(i, str):
            raise TypeError("Values must be strings, got %r" % i)
        try:
            self.get_dbh(k)[k] = i
        except KeyError:
            raise KeyError(k)

    def __delitem__(self, k):
        if not isinstance(k, str):
            raise TypeError("Keys must be strings, got %r" % k)
        try:
            del self.get_dbh(k)[k]
        except KeyError:
            raise KeyError(k)

    def __contains__(self, k):
        if not isinstance(k, str):
            raise TypeError("Keys must be strings, got %r" % k)
        return k in self.get_dbh(k)

class NoHandleError(KeyError):
    # A handle for a certain key cannot be found.
    pass
