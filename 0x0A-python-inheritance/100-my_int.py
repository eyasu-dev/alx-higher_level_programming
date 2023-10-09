#!/usr/bin/python3
"""Module inherits from int
"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
