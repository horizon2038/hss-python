import unittest
from h5ndatetime import datetimeobjectimpl as dtoimpl
from h5ndatetime import datetimeobject as dto

class TestH5nDate(unittest.TestCase):
    def test_year(self):
        current: int = 2005

        year: dto.DateTimeObject = dtoimpl.Year(current)
        self.assertEqual(current, year.current())
        with self.assertRaises(ValueError):
            year.commit(-1)

    def test_month(self):
        current: int = 7

        month: dto.DateTimeObject = dtoimpl.Month(current)
        self.assertEqual(current, month.current())
        with self.assertRaises(ValueError):
            month.commit(-1)
        with self.assertRaises(ValueError):
            month.commit(13)

    def test_day(self):
        current: int = 28

        day: dto.DateTimeObject = dtoimpl.Day(current)
        self.assertEqual(current, day.current())

        with self.assertRaises(ValueError):
            day.commit(0)
        with self.assertRaises(ValueError):
            day.commit(32)

class TestH5nTime(unittest.TestCase):
    def test_hour(self):
        current: int = 1

        hour: dto.DateTimeObject = dtoimpl.Hour(current)
        self.assertEqual(current, hour.current())

        with self.assertRaises(ValueError):
            hour.commit(-1)
        with self.assertRaises(ValueError):
            hour.commit(25)

    def test_minute(self):
        current: int = 1

        minute: dto.DateTimeObject = dtoimpl.Minute(current)
        self.assertEqual(current, minute.current())

        with self.assertRaises(ValueError):
            minute.commit(-1)
        with self.assertRaises(ValueError):
            minute.commit(60)

    def test_second(self):
        current: int = 1

        second: dto.DateTimeObject = dtoimpl.Second(current)
        self.assertEqual(current, second.current())

        with self.assertRaises(ValueError):
            second.commit(-1)
        with self.assertRaises(ValueError):
            second.commit(61)