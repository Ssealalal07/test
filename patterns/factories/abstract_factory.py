from abc import ABC, abstractmethod

#abstract products
class Header(ABC):
    @abstractmethod
    def render(self, text):
        pass

class Table(ABC):
    @abstractmethod
    def render(self, data):
        pass

class Image(ABC):
    @abstractmethod
    def render(self, path):
        pass

class ReportFactory(ABC):
    @abstractmethod
    def create_header(self) -> Header:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_image(self) -> Image:
        pass

    @abstractmethod
    def save(self, filename):
        pass