import unittest
import sys
import os
  
# setting path
sys.path += [os.path.dirname(os.path.dirname(__file__))]
#from h5ntime import abstractdatetime

class TestWrapper(unittest.TestCase):
    print(sys.path)
    '''def test001(self):
        datetime: abstractdatetime.DateTime = datetimeobjectsimpl.DateTimeImpl.datetime(datetimefactoryimpl.DateTimeObjectFactoryImpl(), datetimefactoryimpl.DateTimeObjectsFactoryImpl())
        datetime.current()
        datetime.now()
        datetime.current()'''

if __name__ == "__main__":
    unittest.main()