""" File: test_player_unit.py
    Author: Jeffrey Langemeier
    Description: Unit Tests for the player - unit classes and functions
    Notes: self.dut == Design Under Test
"""
import unittest
from player import unit

class TestUnit(unittest.TestCase):

    def setUp(self):
        self.unit_type = "A"
        self.unit_subtype = "B"
        self.dut = unit.Unit(self.unit_type, self.unit_subtype)

    def tearDown(self):
        self.dut = None

    def test_initialize_unit(self):
        self.assertEqual(self.dut.level, 0)
        self.assertEqual(self.dut.experience, 0)
        self.assertEqual(self.dut.unit_type, self.unit_type)
        self.assertEqual(self.dut.unit_subtype, self.unit_subtype)

    def test_move_unit(self):
        pass

    def test_update_stats(self):
        pass

    def test_update_level(self):
        pass


class TestMilitaryUnit(unittest.TestCase):

    def setUp(self):
        self.unit_subtype = "B"
        self.dut = unit.MilitaryUnit(self.unit_subtype)

    def tearDown(self):
        self.dut = None

    def test_initialize_unit(self):
        self.assertEqual(self.dut.level, 0)
        self.assertEqual(self.dut.experience, 0)
        self.assertEqual(self.dut.unit_type, "Military")
        self.assertEqual(self.dut.unit_subtype, self.unit_subtype)

    def test_attack(self):
        pass


class TestCivilianUnit(unittest.TestCase):

    def setUp(self):
        self.unit_subtype = "B"
        self.dut = unit.CivilianUnit(self.unit_subtype)

    def tearDown(self):
        self.dut = None

    def test_initialize_unit(self):
        self.assertEqual(self.dut.level, 0)
        self.assertEqual(self.dut.experience, 0)
        self.assertEqual(self.dut.unit_type, "Civilian")
        self.assertEqual(self.dut.unit_subtype, self.unit_subtype)

    def test_build(self):
        pass
