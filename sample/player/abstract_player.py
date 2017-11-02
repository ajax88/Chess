from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
