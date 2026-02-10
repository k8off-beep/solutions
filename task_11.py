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
        return self._calories < 200

    def is_delicious(self):
        return True


dessert = Dessert("Печенье", 120)
print(dessert.is_healthy())
print(dessert.get_name())  # Печенье
dessert.set_name('Пирог')
print(dessert.get_name())
dessert.set_calories(200)
print(dessert.get_calories())  # 180

print(dessert.is_healthy())  # True
