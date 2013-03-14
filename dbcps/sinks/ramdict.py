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

class RAMDict(Sink):
    '''
    "Dummy" class for storing all data in memory in a dict.

    >>> s = RAMDict()
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
    >>> s = RAMDict()
    >>> s['blueberry']
    Traceback (most recent call last):
    ...
    KeyError: 'blueberry'
    '''

    def __init__(self, origin=None):
        Sink.__init__(self, origin)
        self.backend = {}
