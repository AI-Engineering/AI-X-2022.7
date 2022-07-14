class FourCalc:
    def set_data(self, first, second):
        self.first = first
        self.second = second

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


calc_0 = FourCalc(4, 2)
calc_1 = FourCalc(2, 2)
calc_2 = FourCalc(4, 0)

print(calc_0.add(), calc_1.add(), calc_0.mul(), calc_1.mul())
# print(calc_2.div())


class MoreCalc(FourCalc):
    # Inheritance
    def __init__(self, first, second, third=12):
        super().__init__(first, second)
        self.third = third

    # Can add new Method
    def pow(self):
        return self.first ** self.second

    # Overriding: Can modified method from inheritance method
    def add(self):
        # print(super().add())  # 상위 클래스의 add의 원본도 사용하고 싶을때
        # return self.first + self.second + self.third
        return super().add() + self.third

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


moreCalc_0 = MoreCalc(4, 2)
moreCalc_1 = MoreCalc(2, 2)
moreCalc_2 = MoreCalc(4, 0)

print(moreCalc_0.add())
print(moreCalc_0.mul(), moreCalc_1.mul(),
      moreCalc_0.pow(), moreCalc_1.pow(), moreCalc_2.div())

