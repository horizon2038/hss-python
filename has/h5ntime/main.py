from abstractdatetime import DateTime
from datetimewrapper import DateTimeImpl
import datetimefactoryimpl
import sys, os

if __name__ == "__main__":
    datetime: DateTime = DateTimeImpl(datetimefactoryimpl.DateTimeObjectFactoryImpl(), datetimefactoryimpl.DateTimeObjectsFactoryImpl())
    datetime.now()
    print(datetime.current())
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    for i in sys.path:
        print(i)