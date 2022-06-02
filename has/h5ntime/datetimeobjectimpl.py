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

from typing import Protocol

class PublishError(Protocol):
    def exception(self, value: any):
        pass

class PublishDateTimeError():
    def exception(self, value: any):
        try:
            raise ValueError("ERROR: invalid DateTime '{0}'".format(value))

        except ValueError as e:
            print(e)

class Year(): #DateTimeObject
    year: int
    publish_yearerror: PublishError

    def __injectexception(self, publish_yearerror: PublishError):
        self.publish_yearerror = publish_yearerror

    def __exception(self, value: int):
        self.publish_yearerror.exception(value)

    def commit(self, value: int):
        if(value <= 0):
            self.__exception(value)
        else:
            self.year = value
    
    def current(self):
        return self.year

    def __init__(self, year: int):
        self.__injectexception(PublishDateTimeError())
        self.commit(year)

class Month(): #DateTimeObject
    month: int
    publish_montherror: PublishError

    def __injectexception(self, publish_montherror: PublishError):
        self.publish_montherror = publish_montherror

    def __exception(self, value: int):
        self.publish_montherror.exception(value)

    def commit(self, value: int):
        if(value <= 0 or 12 < value):
            self.__exception
        else:
            self.month = value

    def current(self):
        return self.month

    def __init__(self, month: int):
        self.__injectexception(PublishDateTimeError())
        self.commit(month)

class Day(): #DateTimeObject
    day: int
    publish_dayerror: PublishError

    def __injectexception(self, publish_dayerror: PublishError):
        self.publish_dayerror = publish_dayerror

    def __exception(self, value: int):
        self.publish_dayerror.exception(value)

    def commit(self, value: int):
        if(value < 0 or 31 < value):
            self.__exception
        else:
            self.day = value

    def current(self):
        return self.day

    def __init__(self, day: int):
        self.__injectexception(PublishDateTimeError())
        self.commit(day)

class Hour(): #DateTimeObject
    hour: int
    publish_hourerror: PublishError

    def __injectexception(self, publish_hourerror: PublishError):
        self.publish_hourerror = publish_hourerror

    def __exception(self, value: int):
        self.publish_hourerror.exception(value)

    def commit(self, value: int):
        if(value < 0 or 24 < value):
            self.__exception
        else:
            self.hour = value

    def current(self):
        return self.hour

    def __init__(self, hour: int):
        self.__injectexception(PublishDateTimeError())
        self.commit(hour)

class Minute(): #DateTimeObject
    minute: int
    publish_minuteerror: PublishError

    def __injectexception(self, publish_minuteerror: PublishError):
        self.publish_minuteerror = publish_minuteerror

    def __exception(self, value: int):
        self.publish_minuteerror.exception(value)

    def commit(self, value: int):
        if(value < 0 or 60 < value):
            self.__exception
        else:
            self.minute = value

    def current(self):
        return self.minute

    def __init__(self, minute: int):
        self.__injectexception(PublishDateTimeError())
        self.commit(minute)

class Second(): #DateTimeObject
    second: int
    publish_seconderror: PublishError

    def __injectexception(self, publish_seconderror: PublishError):
        self.publish_seconderror = publish_seconderror

    def __exception(self, value: int):
        self.publish_seconderror.exception(value)

    def commit(self, value: int):
        if(value < 0 or 60 < value):
            self.__exception
        else:
            self.second = value

    def current(self):
        return self.second

    def __init__(self, second: int):
        self.__injectexception(PublishDateTimeError())
        self.commit(second)