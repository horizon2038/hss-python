from .datetimeobject import DateTimeObject
from .datetimeobjects import DateTimeObjects
from . import datetimeobjectimpl
from . import datetimeobjectsimpl

class DateTimeObjectFactoryImpl():  #Multiple conditional branches are only used for Factory
    def make(self, type: str) -> DateTimeObject:
        if (type == "year"):
            return datetimeobjectimpl.Year(1970)

        elif (type == "month"):
            return datetimeobjectimpl.Month(1)

        elif (type == "day"):
            return datetimeobjectimpl.Day(1)

        elif (type == "hour"):
            return datetimeobjectimpl.Hour(0)

        elif (type == "minute"):
            return datetimeobjectimpl.Minute(0)

        elif (type == "second"):
            return datetimeobjectimpl.Second(0.00)

class DateTimeObjectsFactoryImpl():
    def make(self, type: str) -> DateTimeObjects:
        if (type == "date"):
            return datetimeobjectsimpl.DateImpl()
            
        elif (type == "time"):
            return datetimeobjectsimpl.TimeImpl()