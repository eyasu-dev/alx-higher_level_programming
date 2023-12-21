#!/usr/bin/python3
"""
Holds the class superclass BaseGeometry
"""
<<<<<<< HEAD
Base = __import__('6-base_geometry').BaseGeometry
=======


class BaseGeometry:
    """An empty class"""
>>>>>>> f83b6ecb48e538314d363e2189e189f9076048eb


class BaseGeometry(Base):
    """BaseGeometry class containing area and integer_validator
    """

    def integer_validator(self, name, value):
        """Validates input passed to match conditions provided
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
