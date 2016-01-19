from collections import namedtuple

class Unit(object):

    level_up = [0, 5, 10, 20, 50, 90]

    def __init__(self, unit_type, unit_subtype):
        self.unit_type = unit_type
        self.unit_subtype = unit_subtype
        self.experience = 0
        self.level = 0
        self.stats = {}
        self.actions = {}

    def move(self):
        pass

    def update_stats(self):
        pass

    def update_level(self, experience):
        pass


class MilitaryUnit(Unit):

    def __init__(self, unit_subtype):
        super(MilitaryUnit, self).__init__("Military", unit_subtype)

    def attack(self):
        pass


class CivilianUnit(Unit):

    def __init__(self, unit_subtype):
       super(CivilianUnit, self).__init__("Civilian", unit_subtype)

    def build(self):
        pass
