# TIER 1 - Python Tiers and Expectations

## REPL

- `type()` you can see the type of a variable or object
- `dir()` you can check the directory of any variable or object (even types)
- `help()` checks the docs for any method or object

## Magic methods

Override built-in methods to give certain functionality or info of a specific class

- `__name__` it will contain the name of the script
- `__class__` reference to the type of the current instance
- `__get__` define behavior to get a value
- `__set__` define behavior to set a value
- `__repr__` to return a machine readable representation of a type.
- `__str__` override the `__str__()` method in the class to return a string representation of its object.
- `__unicode__` return an unicode string of a type.

## Duck typing:

It's a concept related to dynamic typing, where the type of the class of an object is less important the methods it defines. It supports all method signatures and attributes.

A way of thinking rather than a type system.
