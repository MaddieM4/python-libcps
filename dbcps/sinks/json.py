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

jsonlib = __import__('json', {})
from dbcps.sinks.core import Sink

class JSON(Sink):
    '''
    >>> import os, shutil
    >>> os.mkdir('tmp')
    >>> s = JSON('tmp/autoflush')
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
    >>> s = JSON('tmp/autoflush')
    >>> print(s['blueberry'])
    pancakes

    >>> d = JSON('tmp/dangerous', False)
    >>> with d:
    ...     d['subliminal_advertising'] = "Eat at Joe's."
    >>> del d
    >>> d = JSON('tmp/dangerous', False)
    >>> print(d['subliminal_advertising'])
    Eat at Joe's.
    >>> d['subliminal_advertising'] = "Sale on sweaters"
    >>> d.flush()
    >>> del d
    >>> d = JSON('tmp/dangerous', False)
    >>> print(d['subliminal_advertising'])
    Sale on sweaters
    >>> d['subliminal_advertising'] = "This won't be saved to disk."
    >>> del d
    >>> d = JSON('tmp/dangerous', False)
    >>> print(d['subliminal_advertising'])
    Sale on sweaters
    >>> shutil.rmtree('tmp')
    '''

    def __init__(self, filename, autoflush = True, origin=None):
        '''
        Autoflush configures whether to flush after ever change. This is not at
        all a performant default! It trades that off for safety. If your code
        is at all performance-critical or deals with nontrivial sizes of data,
        you will want to turn off autoflush, and manually flush with either the
        flush function, or the "with" keyword.
        '''
        Sink.__init__(self, origin)
        self.filename = filename
        self.autoflush = autoflush
        self.backend = {}
        try:
            self.reload()
        except (OSError, IOError): # File doesn't exist yet
            pass

    def reload(self):
        json_obj = jsonlib.load(open(self.filename, 'r'))
        assert isinstance(json_obj, dict)
        self.backend = json_obj

    def __setitem__(self, k, v):
        self.backend[k] = v
        if self.autoflush:
            self.flush()

    def __delitem__(self, k):
        del self.backend[k]
        if self.autoflush:
            self.flush()

    def flush(self):
        jsonlib.dump(self.backend, open(self.filename, 'w'))
