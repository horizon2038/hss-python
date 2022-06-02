from typing import Protocol
from .datetimeobject import DateTimeObject
from .datetimeobjects import DateTimeObjects

class DateTimeObjectFactory(Protocol):
    def make(type: str) -> DateTimeObject:
        pass

class DateTimeObjectsFactory(Protocol):
    def make(self, type: str) -> DateTimeObjects:
        pass