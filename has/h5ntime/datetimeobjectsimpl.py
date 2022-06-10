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

from datetimeobject import DateTimeObject

class DateImpl():
    year: DateTimeObject
    month: DateTimeObject
    day: DateTimeObject

    def __injectdate(self, date: list[DateTimeObject]):
        self.year = date[0]
        self.month = date[1]
        self.day = date[2]

    def current(self):
        date: list[int] = []
        date.append(self.year.current())
        date.append(self.month.current())
        date.append(self.day.current())
        return date

    def commit(self, date: list[int]):
        self.year.commit(date[0])
        self.month.commit(date[1])
        self.day.commit(date[2])

    def __init__(self, date: list[DateTimeObject]):
        self.__injectdate(date)

class TimeImpl():
    hour: DateTimeObject
    minute: DateTimeObject
    second: DateTimeObject

    def __injecttime(self, time: list[DateTimeObject]):
        self.hour = time[0]
        self.minute = time[1]
        self.second = time[2]

    def current(self):
        time: list[int] = []
        time.append(self.hour.current())
        time.append(self.minute.current())
        time.append(self.second.current())
        return time

    def commit(self, time: list[int]):
        self.hour.commit(time[0])
        self.minute.commit(time[1])
        self.second.commit(time[2])

    def __init__(self, time: list[DateTimeObject]):
        self.__injecttime(time)