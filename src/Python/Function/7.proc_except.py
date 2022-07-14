def process_error_print():
    try:
        a = [1, 2]
        print(a[3])
        b = 4 / 0
    except IndexError:
        print("Out of Range for list a")
    except ZeroDivisionError:
        print("Can't divide by 0")

def process_error():

    f = open("tmp.txt", "r")  # finally 수행을 위해...파일하나 생성해서 넣을 것

    try:
        a = [1, 2]
        print(a[3])
        b = 4 / 0
        f = open("foo.txt", "r")

    except ZeroDivisionError as e2:
        print(e2)
    except IndexError as e1:
        print(e1)
    except FileNotFoundError as e3:
        print(e3)
    # except (ZeroDivisionError, IndexError, FileNotFoundError) as e:
    #     print(e)

    # except:
    #     print("ALL Error")

    # finally:
    #     f.close()


# process_error_print()
process_error()

def input_age():
    while True:
        try:
            age = int(input("나이를 입력하세요(숫자만): "))
            if age >= 100:
                print("99세까지만 입력 가능합니다. 다시 입력해주세요.")
            else:
                break
        except ValueError:
            print("다시 입력해주세요! 나이는 숫자만 입력 하세요.")

    return age

print(input_age())


class Bird:
    def fly(self):
        raise NotImplementedError

# Error 발생 (Bird class를 상속받은 Eagle의 경우, raise 예약어를 통하여 fly함수를 반드시 작성해야 함)
# class Eagle(Bird):
#     pass


# Error 확인 후, fly 함수 구현
class Eagle(Bird):
    pass
    # def fly(self):
    #     print("Eagle is Birds")

# eagle = Eagle()
# eagle.fly()

# 직접 예외를 만들어보자. (내장되어 있는 에러가 아니라 직접 작성한 에러로 처리하기 위해)
# 파이썬 내장 클래스인 Exception 클래스를 상속 받아 사용

class MyError(Exception):
    pass
    # def __str__(self):
    #     return "허용하지 않는 별명입니다."

# 1: 내용이 없으면 raise MyError를 발생시키면서 비정상 종료
def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)
# say_nick("천재")
# say_nick("바보")

# 2: 비정상적인 종료를 방지하기 위해 try-except 구문 이용
try:
    say_nick("천재")
    say_nick("바보")
except MyError:
    print("허용하지 않는 별명입니다.")

# 3: MyError as e를 사용하고 싶을때.
# MyError 클래스에 __str__ 메서드 추가해서 해당 메시지가 나오도록 처리
# class MyError(Exception):
#     def __str__(self):
#         return "허용하지 않는 별명입니다."
# try:
#     say_nick("천재")
#     say_nick("바보")
# except MyError as e:
#     print(e)


class NotAllowList(Exception):
    def __str__(self):
        return "List 접근X"

def list_access(in_param_bool, in_param_list):
    if in_param_bool:
        print(in_param_list[:])
    else:
        raise NotAllowList()


# list_access(1, [1, 2, 3])
# list_access(0, [1, 2, 3])

try:
    list_access(0, [1, 2, 3])
    list_access(1, [1, 2, 3])
except NotAllowList as e:
    print(e)