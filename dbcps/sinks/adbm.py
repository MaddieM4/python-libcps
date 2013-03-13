from dbcps.sinks.core import Sink

# Module is renamed in Python 3
try:
    import anydbm
except:
    import dbm as anydbm

class ADBM(Sink):
    '''
    Uses the anydbm module to store data to disc.

    >>> import os, shutil
    >>> os.mkdir('tmp')
    >>> fname = 'tmp/adbm'
    >>> s = ADBM(fname, filemode='c')
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
    >>> s = ADBM(fname)
    >>> print(s['blueberry'].decode())
    pancakes
    >>> shutil.rmtree('tmp')
    '''

    def __init__(self, path, origin = None, filemode='c'):
        Sink.__init__(self, origin)
        self.backend = anydbm.open(path, filemode)
