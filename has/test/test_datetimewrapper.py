import unittest
import sys
sys.path.append('../')

#from h5ntime.abstractdatetime import DateTime

from h5ntime import abstractdatetime
from h5ntime import datetimeobject, datetimeobjects, datetimefactoryimpl, datetimeobjectsimpl

class TestWrapper(unittest.TestCase):
    def test001(self):
        datetime: abstractdatetime.DateTime = datetimeobjectsimpl.DateTimeImpl.datetime(datetimefactoryimpl.DateTimeObjectFactoryImpl, datetimefactoryimpl.DateTimeObjectsFactoryImpl)
        datetime.current()
        datetime.now()
        datetime.current()

if __name__ == "__main__":
    unittest.main()