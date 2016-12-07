import unittest
import datetime

from rwby.utils import to_datetime


class DateUtilsTests(unittest.TestCase):
    def test_to_datetime(self):
        d = datetime.date(day=31, month=12, year=1999)
        self.assertEqual(to_datetime('00:00, 01 January', d),
                         datetime.datetime(day=1, month=1, year=2000, minute=0, hour=0))
        self.assertEqual(to_datetime('01:00, 01 January', d),
                         datetime.datetime(day=1, month=1, year=2000, minute=0, hour=1))
        self.assertEqual(to_datetime('00:05, 01 January', d),
                         datetime.datetime(day=1, month=1, year=2000, minute=5, hour=0))

        d = datetime.date(day=30, month=11, year=1999)
        self.assertEqual(to_datetime('00:00, 01 Dec', d),
                         datetime.datetime(day=1, month=12, year=1999, minute=0, hour=0))
        self.assertEqual(to_datetime('01:00, 01 Dec', d),
                         datetime.datetime(day=1, month=12, year=1999, minute=0, hour=1))
        self.assertEqual(to_datetime('00:05, 01 Dec', d),
                         datetime.datetime(day=1, month=12, year=1999, minute=5, hour=0))

        d = datetime.date(day=30, month=11, year=1999)
        self.assertEqual(to_datetime('00:00', d),
                         datetime.datetime(day=30, month=11, year=1999, minute=0, hour=0))
        self.assertEqual(to_datetime('01:00', d),
                         datetime.datetime(day=30, month=11, year=1999, minute=0, hour=1))
        self.assertEqual(to_datetime('00:05', d),
                         datetime.datetime(day=30, month=11, year=1999, minute=5, hour=0))
