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

# 오늘 날짜 받아오기
import datetime
print(datetime.datetime.today()) # 오늘 날짜를 받아오는 함수이다.
now = datetime.datetime.now()
print(now.year, now.month, now.day)

# 딕셔너리 만들기 dictionary
wintable = {
    '가위':'보', #   이름표:값
    '바위':'가위',
    '보':'바위',
    3:'Tell me'
    }

print(wintable[3])

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

messages = {
    'win':'이겼다',
    'draw':'비겼다',
    'lose':'졌어'
    }

result = rsp('가위','보')
print(messages[result])

result = rsp('바위','바위')
print(messages[result])

result = rsp('가위','바위')
print(messages[result])

# dictionary 수정하기
dict1 ={
    'one':1,
    'two':2,
    'three':3
    }

dict1['one'] = 11 # dictionary 수정하기
print(dict1)

dict1['four'] = 4 # dictionary 추가하기
print(dict1)

del dict1['one']
print(dict1)

print(dict1.pop('two'))
print(dict1)

# dictionary와 반복문
seasons = ['spring','summer','fall','winter']
for season in seasons:
    print(season)

ages ={
    'Tom':12, # key 'Tom' value '12'   
    'Joel':25,
    'Billy':35
    }

for key in ages.keys():
    print(key)

for age in ages.values():
    print(age)

for key, value in ages.items():
    print('이름은 {} 이고, 나이는 {}'.format(key, value))

# 여기서 dictionary는 순서를 보장하지 않는다. 한번씩 모두 나오는 것은 보장되어있다.
# list는 저장하는 순서를 지켜준다.

# list와 dictionary를 비교해보자.
list = [1,2,3,4,5]

print(2 in list) # list에 2가 있는지 확인해라.
print('Tom' in ages) # dict에서 Tom이 있는지 확인해라.

dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}

#dict1.update(dict2)
#print(dict1)

dict2.update(dict1)
print(dict2)

# 튜플 만들기 ( ) 한번 정해지면 값을 바꿀 수 없다.
tuple1 = (1,2,3) 
print(type(tuple1))
tuple2 = 1,2,3       # 이것도 tuple 선언 방법이다.
print(type(tuple2))

tuple3 = tuple(list) # 이것도 tuple 선언 방법이다.
print(type(tuple3)) 

# tuple3[0] = 5 (불가능하다.)

# Tuple 변수의 Packing & UnPacking
c = (3,4)
d,e = c
print(d,e) # Tuple UnPacking

f = d,e
print(f)   # Tuple Packing

d,e = e,d  # Tuple 값 바꾸기
c = d,e
print(c)

# Tuple을 이용한 함수의 리턴값
#for i, v in enumerate(list):
#    print('{}번째 값: {}'.format(i,v))

for a in enumerate(list):
    print('{}번째 값: {}'.format(*a)) #   *a : tuple을 쪼개라.

# while 반복문 
# selected = None
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요.')
# print(selected)

i = 0
while i < len(list):
    print('{} 번째'.format(i))
    i += 1
print()

# break, continue
list_a = [1,2,3,4,5,6,7,8,9,0]
for val in list_a:
    if val % 3 == 0:
        print(val)
        break # 반복문을 종료한다.
