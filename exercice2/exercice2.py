import random

ARMOR_TYPES = ["chobham", "composite", "ceramic"]


class Tank:
    def __init__(self, armor, penetration, armor_type):
        self.armor = armor
        self.penetration = penetration
        self.armor_type = armor_type
        if not (armor_type in ARMOR_TYPES):
            raise Exception(f"Invalid armor type {armor_type}")
        self.tank = "Tank"

    def set_name(self, name):
        self.name = name

    def vulnerable(self, tank):
        real_armor = self.armor
        match self.armor_type:
            case "chobham":
                real_armor += 100
            case "composite":
                real_armor += 50
            case "ceramic":
                real_armor += 50
        if real_armor <= tank.penetration:
            return True
        return False

    def swap_armor(self, othertank):
        tmp = othertank.armor
        othertank.armor = self.armor
        self.armor = tmp
        return othertank

    def __repr__(self):
        if "name" in vars(self):
            return self.name.lower().replace(" ", "-")
        return "Unnamed"

    @staticmethod
    def test_tank_safe(shooter, test_vehicles=[]):
        for t in test_vehicles:
            if not t.vulnerable(shooter):
                print("A tank is safe")
                return
        print("No tank is safe")


if __name__ == "__main__":
    m1 = Tank(600, 670, "chobham")
    if m1.vulnerable(m1):
        print("Vulnerable to self")
    tanks = []
    for i in range(5):
        tanks.append(
            Tank(
                random.randrange(0, 1000),
                random.randrange(0, 1000),
                random.choices(ARMOR_TYPES)[0],
            )
        )
        tanks[i].set_name(f"Tank{str(i)}_Small")
    Tank.test_tank_safe(m1, tanks)
