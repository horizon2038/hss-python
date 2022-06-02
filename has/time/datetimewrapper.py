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
from .datetimeobject import DateTimeObject
from .datetimeobjects import DateTimeObjects
from .datetimefactory import DateTimeObjectFactory, DateTimeObjectsFactory

class DateTimeImpl():
    date: DateTimeObjects
    time: DateTimeObjects

    year: DateTimeObject
    month: DateTimeObject
    day: DateTimeObject
    hour: DateTimeObject
    minute: DateTimeObject
    second: DateTimeObject
    __nowdate: any

    def __injectdatetimeobjectfactory(self, datetimeobjectfactory: DateTimeObjectFactory):
        self.year = datetimeobjectfactory.make("year")
        self.month = datetimeobjectfactory.make("month")
        self.day = datetimeobjectfactory.make("day")

        self.hour = datetimeobjectfactory.make("hour")
        self.minute = datetimeobjectfactory.make("minute")
        self.second = datetimeobjectfactory.make("second")

    def current(self):
        date: str = "{0} {1} {2}".format(self.year.current(), self.month.current(), self.day.current(), self.hour.current(), self.minute.current(), self.second.current())
        return date

    def commit(self, year: int, month: int, day: int):
        self.year.commit(year)
        self.month.commit(month)
        self.day.commit(day)

    def __fetchnowdatetime(self):
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

    def __loadnowdate(self):
        self.__fetchnowdatetime()
        self.__getnowyear()
        self.__getnowmonth()
        self.__getnowday()

    def now(self):
        self.__loadnowdate()
        date: str = self.current()
        return date

    def __init__(self,datetimeobjectfactory: DateTimeObjectFactory):
        self.__injectdatetimeobjectfactory(datetimeobjectfactory)
        self.now() 

if __name__ == "__main__":
    now: DateTime = DateTimeImpl(DateTimeObjectFactoryImpl())
    print(now.commit(2005, 7, 28))
    print(now.current())