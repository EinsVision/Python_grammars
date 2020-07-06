# https://programmers.co.kr/learn/courses/2
print('Hello World')

# function 및 매개 변수

def function():
    print('Hello Function')

function()

def print_round(number): # 매개변수 
    rounded = round(number)
    print(rounded)

print_round(4.7) # 실행인자
print_round(2.2)

# 함수의 return에 대해 알아본다.
def add_10(value):
    result = value + 10
    return result # return은 실행된 즉시 함수는 끝나버린다. 그 뒤의 코드는 실행되지 않느다.

print(add_10(20))

def add_15(value):
    if value < 10:
        return 15
    result = value + 15
    return result

print(add_15(6))
print(add_15(20))

# 함수에서 return 을 두개 !! 
def add(value1, value2):
    r1 = value1
    r2 = value2
    return r1, r2

a, b = add(5, 10)
print('해는 {} {}' .format(a,b))

# format 함수에 대해 알아보자.
number = 20
greeting = '안녕하세요'
place = '문자열 format의 세계'
welcome = '환영합니다.'

base = '{}번 손님, {}. {}에 오신 것을 {}' # 문자열 
print(base.format(number, greeting, place, welcome)) #문자열에 format 기능

# '' 과 문자열
string1 = 'Some text'
string2 = "어떤 텍스트"
string3 = '{}도 어떤 문자열 {}도 문자열'.format(string1, string2)

print(string3) # ('') ("") 아무 차이점이 없다.
long_string = ''' 첫글짜 그리고 
괜찮을까?'''
print(long_string)

# 정수와 실수
num1 = 5
num2 = 5.0
num3 = 5.00

print(num1)
print(num2)
print(num3)

print(0.1 + 0.1 == 0.2) # true
print(0.1+0.1+0.1 == 0.3) # true? False가 나온다.

print(int(5.0)) # 명확하게 얘기할 때 이렇게 쓴다.
print(float(5))
# div1 = 6 / 5    # div = 1.2
# div2 = 6 // 5   # div = 1

# 사용자의 입력을 받기
# mine = input()
# mine = input("가위 바위 보 가운데 하나를 입력하시오.")
mine = '가위'
print('mine: ', mine)

# 리스트 list 사용 (파이썬 자료형)
list1 = ['가위', '바위', '보']
list2 = [1,2,3,4,5]

print(list1) # ['가위', '바위', '보']
print(list2) # [1, 2, 3, 4, 5]
# 값을 꺼내 쓸 때는 []를 사용한다.
print(list1[0])
list1[0] = '바위'
print(list1)
print(list1[-1]) # 뒤에서 첫번째 값을 의미
print(list1[-3]) # 뒤에서 세번째 값을 의미

# 리스트 수정
list3 = [37, 25, 34, 44, 22, 52]
# no.1 list 추가
list3.append(17)
print(list3)

# no.2 list 추가
list3 = list3 + [566]
print(list3)

# list에서 in의 사용
n = 44
ownership = n in list3 # in 연산은 list3에 값 n이 들어 있는지 확인해준다.
print(ownership)

# list를 지우는 연산은 del
# no.1 remove
print(list3)
del list3[0] # list 지우기
print(list3)
# no.2 remove
list3.remove(566)
print(list3)

# for in list
patterns = ['가위', '바위', '보','가위', '바위', '보','가위', '바위', '보']
for pattern in patterns:
    print(pattern) # pattern은 어디에서 왔나? for문이 만든 것이다.

# for in range
# no.1 for문 사용
for i in [1,2,3,4,5]:
    print(i)
print()

# no.2 for문 사용
for i in range(10):
    print(i)

# for in enumerate
names = ['철수', '영희', '영수']
for i, name in enumerate(names): # 값을 두개 받을 때 , 를 사용한다.
    print('{}번: {}'.format(i + 1, name))

# 연습문제 enumerate 쓰기!
days = [31,29,31,30,31,30,31,31,30,31,30,31]
for m,d in enumerate(days): 
    m += 1
    print('{}월의 날짜수는 {}일 입니다.'.format(m,d))

# import의 문법은 해당 모듈을 가져다가 쓰겠다는 것이다.
import math
import random
r = 10
result = 2*math.pi*r
print(result)
print(math.ceil(result))
print(math.floor(result))
print(math.log(result))

candidate = ['가위', '바위', '보']
selected = random.choice(candidate)
print(selected)
selected = random.choice(candidate)
print(selected)
selected = random.choice(candidate)
print(selected)

# internet에 있는 내용을 가져올 수 있다.
def get_web(url):
    import urllib.request # 인터넷의 내용을 가져오는 기능
    response = urllib.request.urlopen(url)
    data = response.read() 
    decoded = data.decode('utf-8')
    return decoded

# url = input('웹 페이지주소?')
# content = get_web(url)
# print(content)

# module 만들기
import my_module # 내가 새롭게 만든 module이다.
print()
print()
print(my_module.random_rsp())

