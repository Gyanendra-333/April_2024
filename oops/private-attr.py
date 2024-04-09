

class Human:

    def __init__(self, f, l, a):
        self.first_name = f
        self.last_name = l
        self._age = a  # private Attribute

        def full_name(self):
            print(f"full name = {self.first_name}")


gyan = Human("Gyanendra", "Insan", 27)
print(gyan)
