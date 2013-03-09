
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

