'''
example:
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class Animal:
    pass


def animal_talk(inst):
    pass

'''
class Animal:
    # def __init__(self):
    #     pass
    def talk(self):
        pass


class Dog(Animal):
    # def __init__(self):
    #     pass

    def talk(self):
        print("Woof-Woof")


class Cat(Animal):
    # def __init__(self):
    #     pass

    def talk(self):
        print("Meoooow")


def pet_see_You(obj):
    obj.talk()

tom = Cat()
jack = Dog()
pet_see_You(tom)
pet_see_You(jack)
