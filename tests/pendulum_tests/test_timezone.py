# -*- coding: utf-8 -*-

from pendulum import Pendulum

from .. import AbstractTestCase


class TimezoneTest(AbstractTestCase):

    def test_in_timezone(self):
        d = Pendulum(2015, 1, 15, 18, 15, 34)
        now = Pendulum(2015, 1, 15, 18, 15, 34)
        self.assertEqual('UTC', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour, now.minute)

        d = d.in_timezone('Europe/Paris')
        self.assertEqual('Europe/Paris', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour + 1, now.minute)

    def test_in_tz(self):
        d = Pendulum(2015, 1, 15, 18, 15, 34)
        now = Pendulum(2015, 1, 15, 18, 15, 34)
        self.assertEqual('UTC', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour, now.minute)

        d = d.in_tz('Europe/Paris')
        self.assertEqual('Europe/Paris', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour + 1, now.minute)

    def test_create_from_format_and_tz(self):
        """Test a use case"""
        d_utc = Pendulum.create_from_format('2016-11-06', '%Y-%m-%d', 'UTC')
        self.assertEqual('UTC', d_utc.timezone_name)
        self.assertPendulum(d_utc, 2016, 11, 6, 0, 0, 0)
        d_colombia = d_utc.in_tz('America/Bogota')
        self.assertEqual('America/Bogota', d_colombia.timezone_name)
        self.assertPendulum(d_colombia, d_utc.year, d_utc.month, 5 , 19 , 0, 0)
        d_israel = d_utc.in_tz('Asia/Jerusalem')
        self.assertPendulum(d_israel, d_utc.year, d_utc.month, d_utc.day , d_utc.hour + 2 , 0, 0)
        
