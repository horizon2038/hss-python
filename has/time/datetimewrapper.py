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

import datetime
from typing import Protocol
from datetimeobject import DateTimeObject
import datetimeobject

class DateTimeFactory(Protocol):
    def makedatetime(type: str) -> DateTimeObject:
        pass

class DateTimeFactoryImpl():  #Multiple conditional branches are only used for Factory

    def makedatetime(self, type: str) -> DateTimeObject:
        if (type == "year"):
            return datetimeobject.Year(1970)

        elif (type == "month"):
            return datetimeobject.Month(1)

        elif (type == "day"):
            return datetimeobject.Day(1)

        elif (type == "hour"):
            return datetimeobject.Hour(0)

        elif (type == "minute"):
            return datetimeobject.Minute(0)

        elif (type == "second"):
            return datetimeobject.Second(0.00)

class DateTime():
    def current(self):
        pass

    def commit(self):
        pass

    def now(self):
        pass

class DateTimeImpl():

    year: DateTimeObject
    month: DateTimeObject
    day: DateTimeObject
    __nowdate: any

    def __injectdatetime(self, datetimefactory: DateTimeFactory):
        self.year = datetimefactory.makedatetime("year")
        self.month = datetimefactory.makedatetime("month")
        self.day = datetimefactory.makedatetime("day")
        self.hour = datetimefactory.makedatetime("hour")
        self.minute = datetimefactory.makedatetime("minute")
        self.second = datetimefactory.makedatetime("second")

    def commit(self, year: int, month: int, day: int):
        self.year.commit(year)
        self.month.commit(month)
        self.day.commit(day)

    def __getnowdate(self):
        self.__nowdate = datetime.datetime.now()

    def __getnowyear(self):
        year = int(self.__nowdate.strftime("%Y"))
        self.year.commit(year)

    def __getnowmonth(self):
        month = int(self.__nowdate.strftime("%m"))
        self.month.commit(month)

    def __getnowday(self):
        day = int(self.__nowdate.strftime("%d"))
        self.day.commit(day)

    def current(self):
        date: str = "{0} {1} {2}".format(self.year.current(), self.month.current(), self.day.current())
        return date

    def __loadnowdate(self):
        self.__getnowdate()
        self.__getnowyear()
        self.__getnowmonth()
        self.__getnowday()

    def now(self):
        self.__loadnowdate()
        date: str = self.date()
        return date

    def __init__(self,datetimefactory: DateTimeFactory):
        self.__injectdatetime(datetimefactory)
        self.now() 

if __name__ == "__main__":
    now = DateTime()
    print(now.commit(-10))
    print(now.now())