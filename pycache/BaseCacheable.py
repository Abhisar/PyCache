from abc import ABCMeta, abstractmethod

class Cacheable(metaclass=ABCMeta):
    @abstractmethod
    def key(self):
        """
        This method has to be implemented by subclass
        :return: Custom Key(Type should be prefferably String) for the Object which is cached
        """
        pass
