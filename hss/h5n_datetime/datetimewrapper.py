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
from datetimeobject import DateTimeObject
from datetimeobjects import DateTimeObjects
from datetimefactory import DateTimeObjectFactory, DateTimeObjectsFactory

class DateTimeImpl():
    date: DateTimeObjects
    time: DateTimeObjects

    __nowdate: any

    def __injectdatetimeobjectfactory(self, datetimeobjectfactory: DateTimeObjectFactory, datetimeobjectsfactory: DateTimeObjectFactory):
        year: DateTimeObject = datetimeobjectfactory.make("year")
        month: DateTimeObject = datetimeobjectfactory.make("month")
        day: DateTimeObject = datetimeobjectfactory.make("day")
        self.date = datetimeobjectsfactory.make("date", [year, month, day])

        hour: DateTimeObject = datetimeobjectfactory.make("hour")
        minute: DateTimeObject = datetimeobjectfactory.make("minute")
        second: DateTimeObject = datetimeobjectfactory.make("second")
        self.time = datetimeobjectsfactory.make("time", [hour, minute, second])

    def currentdate(self):
        date: list[int] = self.date.current()
        return date

    def currenttime(self):
        time: list[int] = self.time.current()
        return time

    def current(self):
        date: list[int] = self.currentdate()
        time: list[int] = self.currenttime()
        return date + time

    def commitdate(self, year: int, month: int, day: int):
        self.date.commit([year, month, day])

    def committime(self, hour: int, minute: int, second: int):
        self.date.commit([hour, minute, second])

    def commit(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        self.commitdate([year, month, day])
        self.committime([hour, minute, second])

    def __fetchnowdatetime(self):
        self.__nowdate = datetime.datetime.now()

    def __getnowdate(self):
        year = int(self.__nowdate.strftime("%Y"))
        month = int(self.__nowdate.strftime("%m"))
        day = int(self.__nowdate.strftime("%d"))
        self.date.commit([year, month, day])

    def __getnowtime(self):
        hour = int(self.__nowdate.strftime("%H"))
        minute = int(self.__nowdate.strftime("%M"))
        second = int(self.__nowdate.strftime("%S"))
        self.time.commit([hour, minute, second])

    def now(self):
        self.__fetchnowdatetime()
        date: list[int] = self.__getnowdate()
        time: list[int] = self.__getnowtime()
        return date

    def __init__(self,datetimeobjectfactory: DateTimeObjectFactory, datetimeobjectsfactory: DateTimeObjectsFactory):
        self.__injectdatetimeobjectfactory(datetimeobjectfactory, datetimeobjectsfactory)