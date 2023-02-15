class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return Person(self.name + other.name)

    def __vowelcount__(self):
        count = 0
        for char in self.name:
            if char in "aeiouAEIOU":
                count += 1
        return count

    def __captialize__(self):
        return self.name.capitalize()

    def __reverseit__(self):
        return self.name[::-1]


    def __iter__(self):
        def value_generator():
            current = self.name
            for x in current:
                yield x

        return value_generator()

    def __namezip__(self, other):
        return list(zip(list(self), list(other)))

    def __repr__(self):
        return f"Person('{self.name}')"

    def __lenisodd__(self):
        if len(self) % 2 == 0:
            return False
        return True

