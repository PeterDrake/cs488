# Two ways to do the same thing

class InheritedValueCounter(dict):  # An InheritedValueCounter is-a dict
    def count_values(self):
        return len(set(self.values()))
    def __repr__(self):
        return f'InheritedValueCounter: {super().__repr__()}'

ivc = InheritedValueCounter()
ivc['a'] = 1
ivc['b'] = 2
ivc['c'] = 1

print(ivc)
print(ivc.count_values())


class ComposedValueCounter:  # A ComposedValueCounter has-a dict
    def __init__(self):
        self.data = dict()
    def __setitem__(self, key, value):  # Delegate method
        self.data[key] = value
    def __repr__(self):
        return f'ComposedValueCounter: {self.data.__repr__()}'
    def count_values(self):
        return len(set(self.data.values()))

cvc = ComposedValueCounter()
cvc['a'] = 1
cvc['b'] = 2
cvc['c'] = 1

print(cvc)
print(ivc.count_values())


# Inheritance exposes methods you might not want in the subclass
print(ivc['a'])


# Inheritance breaks encapsulation

class A:
    def foo(self):
        return self.bar()
    def bar(self):
        return 1

class B(A):
    def bar(self):
        return 2

a = A()
print(a.foo(), a.bar())
b = B()
print(b.foo(), b.bar())

# B's foo behaves differently from A's foo, but there's no way to predict this without looking inside A's code!


# Subclass explosion

class OneFoot:
    def number(self):
        return 1
    def unit(self):
        return 'foot'
    def __repr__(self):
        return f'{self.number()} {self.unit()}'

class TwoFoot(OneFoot):
    def number(self):
        return 2

class OneMeter(OneFoot):
    def unit(self):
        return 'meter'

print(OneFoot())
print(TwoFoot())
print(OneMeter())

# If you wanted 5 different numbers and 5 different units, you'd have to define 25 classes!

class OneMaker:
    def number(self):
        return 1

class TwoMaker:
    def number(self):
        return 2

class FootMaker:
    def unit(self):
        return 'foot'

class MeterMaker:
    def unit(self):
        return 'meter'

class NumberUnit:
    def __init__(self, number, unit):
        self.number_maker = number
        self.unit_maker = unit
    def __repr__(self):
        return f'{self.number_maker.number()} {self.unit_maker.unit()}'

print(NumberUnit(OneMaker(), FootMaker()))
print(NumberUnit(TwoMaker(), FootMaker()))
print(NumberUnit(OneMaker(), MeterMaker()))
print(NumberUnit(TwoMaker(), MeterMaker()))

# How many classes now for 5 different numbers and 5 different units?
