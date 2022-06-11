import unittest
from h5ntime import datetimeobjectimpl as dtoimpl
from h5ntime import datetimeobject as dto

class TestH5ntime(unittest.TestCase):
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