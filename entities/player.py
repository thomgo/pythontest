class Player:
    def __init__(self, name: str, age: int):
        self._name = None
        self._age = None
        # call all setters for the private properties
        self.hydrate(name, age)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if len(name) > 2 and len(name) <= 25:
            self._name = name
            return self
        raise Exception("Name must contain between 3 and 25 characters")
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if age > 10 and age < 99:
            self._age = age
            return self
        raise Exception("You have to be a leats 11 to play")

    # Should expect a set or dict and test for method existence to be more efficient
    def hydrate(self, name: str, age: int):
        self.name = name
        self.age = age