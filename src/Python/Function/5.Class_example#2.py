# 모델을 생성할 때 클래스(Class)를 많이 사용해서 구현
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
# Class 실습 (상속, super)
# example #1: 단순 상속 (computer, notebook)
# example #2: rectangle, square, cube의 면적 및 넓이 구하기.

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def browse(self):
        print('web 서핑')

    def calc(self):
        print('Calculate, ML, DL,...')

# Laptop class는 computer class를 상속 받아서 구현
class Laptop(Computer):
    def __init__(self, cpu, ram, battery):
        # 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용
        # 컴퓨터 클래스의 init을 그대로 사용
        # super를 사용했기 때문에 init에서 cpu, ram을 self에 넣는 코드 불필요
        # init은 생성자에 의해 객체를 생성하면 무조건 실행되는 부분
        # a=computer()를 통해 객체가 생성이 되면
        # cpu, ram 이라는 객체(메모리에 적재되는 변수)가 생성되면서 객체 생성 시 생성자 파라미터에 넘겨준 값을 해당 객체 변수에 할당
        # 이 부분이 부모 클래스인 computer에 포함되어 있으므로 super를 이용하여 사용 가능
        super().__init__(cpu, ram)
        self.battery = battery

    def move(self):
        print("노트북은 이동 가능")

# Example#2: Rectangle 면적, 넓이 구하기.
# 상속 및 Super 사용 전후 비교..rectangle example로 다시
class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2*self.w + 2*self.h


    # super(하위클래스, 하위 클래스 객체) 테스트를 위한 메서드 작성 (cube 작성 시)
    def area_tmp(self):
        print("inh==>inh: 상속에 상속")
        return self.w * self.h



class Square:
    def __init__(self, w):
        self.w = w

    def area(self):
        return self.w**2

    def perimeter(self):
        return 4*self.w

class SquareInh(Rect):
    def __init__(self, w):
        # super를 사용함으로써, 코드를 줄일 수 있음
        # 즉, self에 할당하는 부분을 포함하여
        # 면적과 둘레를 구하는 함수를 부모 클래스(Rect(직사각형))에 있는 것 그대로 사용해도 무관함
        super().__init__(w, w)

    # super(하위클래스, 하위 클래스 객체) 테스트를 위한 메서드 작성
    def area_tmp(self):
        print("inh: 상속")
        return self.w * self.w

# super() vs super(SquareInh, self)
# 코드를 보다보면 종종 위와 같은 케이스 발견
# super(SquareInh, self): SquareInh는 하위 클래스의 이름, 하위 클래스의 object
# 탐색 범위가 달라짐 (다중 상속이나 상속->상속일 경우)
# 예제를 위해 Rect, Square class에 area_tmp 메소드 추가 및 Cube class 추가
class Cube(SquareInh):
    def surface_area(self):
        sur_area = super(SquareInh, self).area_tmp()  # 상속에 상속(SquareInh --> Rect)
        # 정육면체의 넓이는 w*h*6
        return sur_area * 6

    def volumn(self):
        vol = super().area_tmp() # 상속(SquareInh)
        return vol * self.w

# 단순 선형 회귀 클래스로 구현
class LinearRegressionModel(nn.Module): # torch.nn.Module을 상속받는 단순 회귀 모델 클래스 구현
    def __init__(self, in_dim, out_dim):
        # nn.Module 클래스의 속성들을 가지고 초기화, 객체가 생성될때 자동으로 수행(호출)
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        # linear 멤버(nn.Module)에 nn.Linear(1, 1) 할당
        self.linear = nn.Linear(self.in_dim, self.out_dim)

    def forward(self, train_x):
        return self.linear(train_x) # WX 값 리턴

if __name__ == "__main__":

    # 컴퓨터 랩탑 상속 예제
    laptop = Laptop("Intel CPU 2G", "8GB", "100%")
    print(laptop.cpu)
    laptop.move()

    # rect, square class example
    rect = Rect(2, 4)
    print(rect.area(), rect.perimeter())
    squar = Square(4)
    print(squar.area(), squar.perimeter())

    squar_inh = SquareInh(4)
    print(squar_inh.area(), squar_inh.perimeter())

    cube = Cube(3)
    print(cube.surface_area())
    print(cube.volumn())