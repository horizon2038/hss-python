from .datetimeobject import DateTimeObject

class DateImpl():
    year: DateTimeObject
    month: DateTimeObject
    day: DateTimeObject

    def __injectdatetime(self, date: list[DateTimeObject]):
        self.year = date[0]
        self.month = date[1]
        self.day = date[2]

    def current(self):
        date: list[int]
        date[0] = self.year
        date[1] = self.month
        date[2] = self.day
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

    def __injectdatetimeobjectfactory(self, time: list[DateTimeObject]):
        self.hour = time[0]
        self.minute = time[1]
        self.second = time[2]

    def current(self):
        time: list[int]
        time[0] = self.hour
        time[1] = self.minute
        time[2] = self.second
        return time

    def commit(self, time: list[int]):
        self.hour.commit(time[0])
        self.minute.commit(time[1])
        self.second.commit(time[2])

    def __init__(self, time: list[DateTimeObject]):
        self.__injecttime(time)