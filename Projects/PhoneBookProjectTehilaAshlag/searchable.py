from abc import ABC, abstractmethod

class Compareable(ABC):
    @abstractmethod
    def compare_name(self, queriedName):
        pass