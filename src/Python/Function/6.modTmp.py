def add(a, b):
    return a + b

def mul(a, b):
    return a * b

class Calculator:
    def __init__(self):
        self.a = 3
        self.b = 4

if __name__ == "__main__":
    calc = Calculator()

    print(add(3, 4))
    print(mul(3, 4))

    print(f'result of class: {calc.a + calc.b}')
