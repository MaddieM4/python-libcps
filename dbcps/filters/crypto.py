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

import ejtp.crypto
from dbcps.filters.core import Filter

class CryptoFilter(Filter):
    def __init__(self, target=None, origin=None, encryptor=None):
        '''
        >>> from dbcps.sinks.ramdict import RAMDict
        >>> from __future__ import print_function
        >>> f = CryptoFilter(RAMDict(), encryptor = ['rotate', 91]);
        >>> f['shihad'] = 'band'
        >>> print(f['shihad'].decode())
        band
        >>> "shihad" in f
        True
        >>> "shihat" in f
        False
        >>> del f["shihad"]
        >>> "shihad" in f
        False
        >>> print(f['shihad'].decode())
        Traceback (most recent call last):
        ...
        KeyError: 'shihad'
        '''
        Filter.__init__(self, target, origin)
        self.encryptor = encryptor

    def encrypt(self, value):
        return self.encryptor.encrypt(value).export()

    def decrypt(self, value):
        return self.encryptor.decrypt(value).export()

    @property
    def encryptor(self):
        return self.attributes['encryptor']

    @encryptor.setter
    def encryptor(self, encryptor):
        self.attributes['encryptor'] = ejtp.crypto.make(encryptor)

    def __setitem__(self, k, v):
        k = self.encrypt(k)
        v = self.encrypt(v)
        self.target[k] = v

    def __getitem__(self, k):
        ke = self.encrypt(k)
        try:
            v = self.target[ke]
        except:
            raise KeyError(k) # Don't expose encrypted key data in traceback
        return self.decrypt(v)

    def __delitem__(self, k):
        ke = self.encrypt(k)
        try:
            del self.target[ke]
        except:
            raise KeyError(k) # Don't expose encrypted key data in traceback

    def __contains__(self, k):
        k = self.encrypt(k)
        return k in self.target
