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
        if isinstance(self._calories, (int, float)):
            return self._calories < 200
        return False

    def is_delicious(self):
        return True
