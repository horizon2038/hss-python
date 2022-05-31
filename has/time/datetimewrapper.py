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
from datetimeobject import Checkable
import datetimeobject

class DateTimeFactory(Protocol):
    def makedatetime(type: str) -> Checkable:
        pass

class DateTimeFactoryImpl():  #Multiple conditional branches are only used for Factory

    def makedatetime(self, type: str) -> Checkable:
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

class Date():

    year: Checkable
    month: Checkable
    day: Checkable
    __nowdate: any

    def __injectdate(self, datetimefactory: DateTimeFactory):
        self.year = datetimefactory.makedatetime("year")
        self.month = datetimefactory.makedatetime("month")
        self.day = datetimefactory.makedatetime("day")

    def __getnowdate(self):
        self.__nowdate = datetime.datetime.now()

    def check(self, year: int, month: int, day: int):
        self.year.check(year)
        self.month.check(month)
        self.day.check(day)

    def __getnowyear(self):
        year = int(self.__nowdate.strftime("%Y"))
        self.year.check(year)

    def __getnowmonth(self):
        month = int(self.__nowdate.strftime("%m"))
        self.month.check(month)

    def __getnowday(self):
        day = int(self.__nowdate.strftime("%d"))
        self.day.check(day)

    def date(self):
        date: str = "{0} {1} {2}".format(self.year.year, self.month.month, self.day.day)
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
        self.__injectdate(datetimefactory)
        self.now() 

class Time():

    hour: Checkable
    minute: Checkable
    second: Checkable
    __nowtime: any

    def __injecttime(self, datetimefactory: DateTimeFactory):
        self.hour = datetimefactory.makedatetime("hour")
        self.minute = datetimefactory.makedatetime("minute")
        self.second = datetimefactory.makedatetime("second")

    def __getnowtime(self):
        self.__nowtime = datetime.datetime.now()

    def check(self, hour: int, minute: int, second: float):
        self.hour.check(hour)
        self.minute.check(minute)
        self.second.check(second)

    def __getnowhour(self):
        hour = int(self.__nowtime.strftime("%H"))
        self.hour.check(hour)

    def __getnowminute(self):
        minute = int(self.__nowtime.strftime("%M"))
        self.minute.check(minute)

    def __getnowsecond(self):
        second = float(self.__nowtime.strftime("%S.%f"))
        self.second.check(second)

    def time(self):
        time: str = "{0} {1} {2}".format(self.hour.hour, self.minute.minute, self.second.second)
        return time

    def __loadnowtime(self):
        self.__getnowtime()
        self.__getnowhour()
        self.__getnowminute()
        self.__getnowsecond()

    def now(self):
        self.__loadnowtime()
        time: str = self.time()
        return time

    def __init__(self,datetimefactory: DateTimeFactory):
        self.__injecttime(datetimefactory)
        self.now() 

class DateTime():
    date: Date
    time: Time

    def __init__(self):
        self.date = Date(DateTimeFactoryImpl())
        self.time = Time(DateTimeFactoryImpl())

    def split(self, datetime: str):
        splitted_datetime = datetime.split()
    
    def check(self, value: int):
        self.date.check(value, value, value)
        self.time.check(value, value, value)
    
    def datetime(self):
        datetime = "{0} {1}".format(self.date.date(), self.time.time)

    def now(self):
        datetime: str = "{0} {1}".format(self.date.now(), self.time.now())
        return datetime

if __name__ == "__main__":
    now = DateTime()
    print(now.check(-10))
    print(now.now())