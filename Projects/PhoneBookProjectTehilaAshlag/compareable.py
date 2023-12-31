from abc import ABC, abstractmethod

class Compareable(ABC):
    @abstractmethod
    def compare(self, unique_val):
        pass