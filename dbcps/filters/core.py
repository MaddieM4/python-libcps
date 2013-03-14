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

class Filter(object):
    '''
    Composable filter base class.
    '''
    def __init__(self, target=None, origin = None):
        self.attributes = {}
        self.target = target
        self.origin = origin

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
        if isinstance(target, Filter):
            self._target = target
            target._origin = self
        elif target == None:
            self._target = None
        else:
            raise TypeError("Expected Filter or None, got %r" % target)

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        if isinstance(origin, Filter):
            origin.target = self
        elif origin == None:
            self._origin = None
        else:
            raise TypeError("Expected Filter or None, got %r" % origin)

    def set_attributes(self, **kwargs):
        self.attributes.update(kwargs)

    def __setitem__(self, k, v):
        raise NotImplementedError("Subclasses of dbcps.filter.Filter must define __setitem__")

    def __getitem__(self, k):
        raise NotImplementedError("Subclasses of dbcps.filter.Filter must define __getitem__")

    def __delitem__(self, k):
        raise NotImplementedError("Subclasses of dbcps.filter.Filter must define __delitem__")

    def __contains__(self, k):
        raise NotImplementedError("Subclasses of dbcps.filter.Filter must define __contains__")

    # Flushing

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.flush()

    def flush(self):
        if hasattr(self.target, 'flush'):
            self.target.flush()
