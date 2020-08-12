
from abc import ABCMeta, abstractmethod

class ICommand:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, *args, **kwargs) -> any: raise NotImplementedError
    
