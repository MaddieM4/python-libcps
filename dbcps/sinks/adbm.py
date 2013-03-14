'''
This file is part of the Python CPS library.

The Python CPS library is free software: you can redistribute it 
and/or modify it under the terms of the GNU Lesser Public License as
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

the Python CPS library is distributed in the hope that it will be 
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser Public License for more details.

You should have received a copy of the GNU Lesser Public License
along with the Python CPS library.  If not, see 
<http://www.gnu.org/licenses/>.
'''

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

    def __contains__(self, k):
        if (anydbm.__name__ == 'anydbm'):
            return k in self.backend
        elif (anydbm.__name__ == 'dbm'):
            return k.encode('utf-8') in self.backend
        else:
            raise NotImplementedError("anydbm wasn't imported via anydbm or dbm, not sure what's going on!")
