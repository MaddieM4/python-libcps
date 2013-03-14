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

redislib = __import__("redis", {})
from dbcps.sinks.core import Sink

class Redis(Sink):
    '''
    Uses the redis module to store data to a key value store.

    >>> from __future__ import print_function
    >>> s = Redis()
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
    >>> s = Redis()
    >>> print(s['blueberry'].decode())
    pancakes
    '''

    def __init__(self, origin=None, host='localhost', port=6379):
        Sink.__init__(self, origin)
        self.backend = redislib.Redis(host, port)
