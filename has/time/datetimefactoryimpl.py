"""
 Copyright (c) 2022 horizon2038

 Permission is hereby granted, free of charge, to any person obtaining a copy of
 this software and associated documentation files (the "Software"), to deal in
 the Software without restriction, including without limitation the rights to
 use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 the Software, and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 """

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
    def make(self, type: str, datetimeobjects: list[DateTimeObject]) -> DateTimeObjects:
        if (type == "date"):
            return datetimeobjectsimpl.DateImpl(datetimeobjects)
            
        elif (type == "time"):
            return datetimeobjectsimpl.TimeImpl(datetimeobjects)