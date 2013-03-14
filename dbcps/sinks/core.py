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

from dbcps.filters.core import Filter

class Sink(Filter):
    '''
    Filter that provides actual raw access to data, 
    and cannot forward to targets.

    If self.backend is present, dict indexing functions will use that as the
    source and target for their operations. Otherwise, you must define your
    own versions of those functions.
    '''

    def __init__(self, origin=None):
        Filter.__init__(self, origin = origin)

    @property
    def target(self):
        return None

    @target.setter
    def target(self, target):
        if target != None:
            raise TypeError("Sinks can only have their target set to None")
        self._target = None

    def __setitem__(self, k, v):
        if hasattr(self, "backend"):
            self.backend[k] = v
        else:
            raise NotImplementedError("Sink has no backend or __setitem__ override")

    def __getitem__(self, k):
        if hasattr(self, "backend"):
            return self.backend[k]
        else:
            raise NotImplementedError("Sink has no backend or __getitem__ override")

    def __delitem__(self, k):
        if hasattr(self, "backend"):
            del self.backend[k]
        else:
            raise NotImplementedError("Sink has no backend or __delitem__ override")

    def __contains__(self, k):
        if hasattr(self, "backend"):
            return k in self.backend
        else:
            raise NotImplementedError("Sink has no backend or __contains__ override")

