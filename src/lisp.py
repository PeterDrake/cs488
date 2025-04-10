from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def evaluate(self):
        pass

class Number(Expression):
    def __init__(self, n):
        self.n = n
    def evaluate(self):
        return self.n

class Operation(Expression):  # The warning implementing abstract methods can be ignored
    def __init__(self, *operands):
        self.operands = operands

class Add(Operation):
    def evaluate(self):
        result = 0
        for r in self.operands:
            result += r.evaluate()
        return result

class Multiply(Operation):
    def evaluate(self):
        result = 1
        for r in self.operands:
            result *= r.evaluate()
        return result

exp = Add(Number(2), Number(3))
print(exp.evaluate())

# def parse(expression):
#     operators = {'+': Add, '*': Multiply}
#     if type(expression) is tuple:
#         operands = (parse(e) for e in expression[1:])
#         return operators[expression[0]](*operands)
#     return Number(expression)
#
# exp = parse(('*', 2, ('+', 3, 4)))
# print(exp.evaluate())

