#! /usr/bin/env python

from robot_control.rotate_robot import RobotControl
import unittest


class MyTestSuite(unittest.TestCase):

    def setUp(self):
        self.rc = RobotControl()

    def test_CaseA(self):

        speed, angle = self.rc.convert_degree_to_rad(60, 90)
        self.assertEquals(angle, 1.57, "1.57!=1.57")
        self.rc.shutdownhook()

    def test_CaseB(self):

        speed, angle = self.rc.convert_degree_to_rad(60, -90)
        print angle
        self.assertEquals(angle, 1.57, "1.57!=1.57")
        self.rc.shutdownhook()