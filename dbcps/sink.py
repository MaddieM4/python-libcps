from dbcps.filter import Filter

class Sink(Filter):
    '''
    Filter that provides actual raw access to data, 
    and cannot forward to targets.
    '''
    @target.setter
    def target(self, target):
        if target != None:
            raise TypeError("Sinks can only have their target set to None")
        self._target = None
