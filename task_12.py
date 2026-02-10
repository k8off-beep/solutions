class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def get_name(self):
        return self._name

    def get_calories(self):
        return self._calories

    def set_name(self, name):
        self._name = name

    def set_calories(self, calories):
        self._calories = calories

    name = property(get_name, set_name)
    calories = property(get_calories, set_calories)

    def is_healthy(self):
        if self._calories is None:
            return False
        return float(self._calories) < 200

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        Dessert.__init__(self, name, calories)
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor

    def set_flavor(self, flavor):
        self._flavor = flavor

    flavor = property(get_flavor, set_flavor)

    def is_delicious(self):
        if self._flavor == 'black licorice':
            return False

        return True
