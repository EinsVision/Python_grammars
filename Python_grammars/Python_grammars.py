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
listd = [1,2,3,4,5]

print(2 in listd) # list에 2가 있는지 확인해라.
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

tuple3 = tuple(listd) # 이것도 tuple 선언 방법이다.
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

for a in enumerate(listd):
    print('{}번째 값: {}'.format(*a)) #   *a : tuple을 쪼개라.

# while 반복문 
# selected = None
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요.')
# print(selected)

i = 0
while i < len(listd):
    print('{} 번째'.format(i))
    i += 1
print()

# break, continue
list_a = [1,2,3,4,5,6,7,8,9,0]
for val in list_a:
    if val % 3 == 0:
        print(val)
        break # 반복문을 종료한다.

# try, except

list3 = []
try:
    list3[0] # IndexError: list index out of range
except IndexError: # error가 발생할 경우 따로 처리를 해줄 수 있다. 프로그램이 멈추는 경우를 막을 수 있다.
    print('범위를 벗어났습니다.')

try:
    import my_module
except ImportError:
    print("모듈이 없습니다.")

try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# error의 이름을 모를 경우 
try:
    list4 = []
    print(list4[0])

    text = 'abc'
    number = int(text)
except Exception as ex: # error의 이름을 모를 경우 
    print("error가 발생했습니다.", ex) # error의 종류를 알 수 있다.

# error raise 에러 발생
def rsp1(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError            # error를 발생시키는 문법
    if yours not in allowed:
        raise ValueError

try:
    rsp1('가위','바')
except ValueError:
    print('잘못된 값입니다.')

school = {'1반': [174,167,526,546],
          '2반': [223,442,444,222]
          }

try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print('190을 넘는 학생이 있습니다.')
                raise StopIteration # 실행 흐름을 끊는다.
except StopIteration:
    print('190 이상 존재!')

# 논리연산 더 알아보기
def return_false():
    print('함수 return false')
    return False

def return_true():
    print('함수 return true')
    return True

a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)


# bool 평가! 
print(bool(0))
print(bool(-12))
print(bool(None))
print(bool('hi'))

# list의 다양한 기능
list5 = [113,246,33,555,34]
print(list5.index(246))
try:
    print(list5.index(247))
except ValueError:
    print('index is none at list5')
# list를 덧붙일 수 있다.
list6 = [1,2,3] + [4,5,6]
print(list6)

list6.extend([9,10,11])
print(list6)

list6.insert(2,999)
print(list6)

list6.insert(-1,9999)
print(list6)

list6.sort() # 오름차순으로 정리한다.
print(list6)

list6.reverse() # 내림차순으로 정리한다.
print(list6)


def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)

    else:
        return None

# list와 문자열
print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))

my_list = [1,2,3,4,5,6]
print(my_list[0])

str = "hello world"
print(str[0])

print('h' in str)
print('z' in str)

print(str.index('r'))

words_list = str.split() # 공백으로 string을 잘라서 list를 만들어 준다.
print(words_list)

time_list = "10:34:55"
time_str = time_list.split(':') # : 를 기준으로 string을 잘라서 list를 만들어 준다.
print(time_str)

":".join(time_str)
print(time_str)

" ".join(words_list)
print(words_list)

# Slice ( list의 일부분을 가져오는 것을 말한다. )
list7 = [1,2,3,4,5]
print(list7[1])
print(list7[1:4]) # [2, 3, 4] 출력!

text = "hello world"
print(text[1:len(text)]) # 특정 위치부터 끝까지 가져오는 방법이다.
print(text[2:])

# Slice Step
a = list(range(20))
print(a)

print(a[5:15])
print(a[5:15:2]) # 2가 step이다.
print(a[5:15:3]) # 3이 step이다.
print(a[14:4:-1]) # 3이 step이다.
print(a[::3])

# Slie로 List 수정하기
numbers = list(range(10))
print(numbers)
del numbers[0]
print(numbers)
del numbers[:5]
print(numbers)

numbers[1:3] = [77,88,99] 
print(numbers) # [6, 77, 88, 9]

# 자료형 다루기
s = "Hello World"
print(type(s)) # <class 'str'>  문자열

f = 3.14
print(type(f)) # <class 'float'> float 

i = 43
print(type(i)) # <class 'int'>

print(isinstance(42, int)) 
print(isinstance(42, float)) 
print()

# 연습문제
my_list = [1, 2, 3]
my_dict = {"풀": 800, "색연필": 3000}
my_tuple = (1, 2, 3)
number = 10
real_number = 3.141592

print(type(my_list))
print(type(my_dict))
print(type(my_tuple))
print(type(number))
print(type(real_number))

# class와 인스턴스
numbers = list(range(10))
print(numbers)
print(type(numbers))

char = list('hello')
print(char)
print(type(char))

# 인스턴스: 만들어져서 사용가능한 list를 말한다.
# class: type을 말한다.
# 연습문제
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("당연히 list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")

# class 만들기
# class 선언
class Human():
    '''사람'''

# 인스턴스 생성
person1 = Human()
person2 = Human()

print(person1)
print(type(person1))

person1.langague = '한국어'
person2.langague = '영어'

person1.name = '한국사람'
person2.name = '인도사람'
print(person1.langague)
print(person2.langague)

def speak(person):
    print('{} 이 {}로 말합니다.'.format(person.name, person.langague))

Human.speak = speak

print(person1.speak())
print(person2.speak())

# class modeling
class BeingHuman():
    ''' 사람이 되어라'''
    # 특수한 메소드
    def __init__(self):
        '''초기화 함수'''
        print('__init__ 실행')

    def __str__(self):
        '''문자열화 함수'''
        print('__str__ 실행')
        return '{} (몸무게) {} (kg) '.format(self.name, self.weight)
        
    def create_human(name, height, weight):
        person = BeingHuman()
        person.name = name
        person.height = height
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print('{}가 먹어서 {}가 되었습니다.'.format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print('{}가 걸어서 {}가 되었습니다.'.format(self.name, self.weight))

    def speak(self, message):
        print(message)

print()
person = BeingHuman.create_human('egoing', 172, 70)
print(person)

person.eat()
person.walk()
person.eat()
person.eat()
person.eat()
person.eat()
person.eat()
person.eat()
person.eat()
person.eat()
person.speak('I wanna speak English')

# 매소드 이해하기
# 메소드는 함수와 비슷하다.
# 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수


class Car():
    '''자동차'''

    def run(self):
        print("{}가 달립니다.".format(self.name))

taxi = Car()
taxi.name = "택시"
taxi.run()

# 상속과 다형성
class animal():          # 부모 class 
    def walk(self):
        print('걷는다.')
    def eat(self):
        print('먹는다.')
    def greet(self):
        print(' 인사한다.')

class Human_heri(animal): # 상속의 개념이다. (자식 class)
    #def walk(self):
    #    print('걷는다.')
    #def eat(self):
    #    print('먹는다.')
    def wave(self):
        print('손을 흔든다.')
    def greet(self): # 단순 오버라이드
        self.wave()
        super().greet()

class dog(animal): # 상속의 개념이다. (자식 class)
    #def walk(self):
    #    print('걷는다.')
    #def eat(self):
    #    print('먹는다.')
    def wag(self):
        print('꼬리를 흔든다.')
    def greet(self): # 단순 오버라이드
        self.wag()
        super().greet()

print()
person5 = Human_heri()
person5.walk()
person5.eat()
person5.wave()
person5.greet()
print()


Dog = dog()
Dog.walk()
Dog.eat()
Dog.wag()
Dog.greet()

# List Comprehension
areas = []
for i in range(1,11):
    areas = areas + [i*i] 

print(areas)

area = [i*i for i in range(1,11)]
print(area)

# 특정 조전을 만족하는 list를 넣는다.
area2 = [i*i for i in range(1,11) if i % 2 == 0]
print(area2)

#area3 = [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
#print(area3)

# datetime 날짜와 시간 다루기
import datetime
print(datetime.datetime.now())

start_time = datetime.datetime.now()
print(type(start_time))        # <class 'datetime.datetime'>

start_time = start_time.replace(year=2017, month=2, day=1)
print(start_time)

# 연습문제
import datetime

def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = (christmas_2030 - datetime.datetime.now()).days
    return days

print("{}일".format(days_until_christmas()))

# timedelta
hundred = datetime.timedelta(days=100)              # timedelta       
hundred_before = datetime.timedelta(days=-100)      # timedelta
print(hundred)

# 현재 + 100일 
print(datetime.datetime.now() + hundred)
print(type(datetime.datetime.now() + hundred))

# 현재 - 100일 
print(datetime.datetime.now() + hundred_before)
print(type(datetime.datetime.now() + hundred_before))

# 하루만 더 해보자.
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print(tomorrow)

hundred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days=+100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))