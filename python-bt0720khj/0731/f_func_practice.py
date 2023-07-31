#책 199p
# 700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지
# 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현

# 함수 정의
# 반환값x
# 함수 이름 : vending_machine()
# 매개변수 : 정수 money

def vending_machine(money):
    #음료수 가격
    drink_price = 700

    # 음료수 개수 & 잔돈 계산
    num_drink = money // drink_price #돈을 음료수 가격으로 나눈 몫이 음료수 개수
    change = money % drink_price # 돈을 음료수 가격으로 나눈 나머지가 잔돈

    #출력
    print(f'{money}원을 넣었을 때: {num_drink}잔의 음료수, 잔돈{change}원')
vending_machine(3000)
#3000원을 넣었을 때:4잔의 음료수, 잔돈 200원

# 1. 'Hello, World' 를 출력하는 함수를 작성
def hello_world():
    print('Hello World')
hello_world()
# 2. 주어진 두 숫자의 합을 반환하는 함수를 작성
def add(a, b):
    return a + b
print(add(3, 2))

# 3. 주어진 숫자 리스트의 합을 반환하는 함수를 작성
#반환하는 함수를 작성
def sum_numbers(numbers):
    return sum(numbers)
print(sum_numbers([1, 2, 3, 4, 5]))

# 4. 이름을 인자로 받아 인사하는 함수를 작성
# 만약 이름이 주어지지 않은 경우, "Guest" 라는 이름으로 인사

def greet(name="Guest"):
    print(f'Hello, {name}')
greet('Seungah')
greet()

