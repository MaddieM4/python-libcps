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
