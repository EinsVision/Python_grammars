import numpy as np
# 1. numpy는 다차원 배열을 나타내기 위한 라이브러리이다.

# 2. list 생성
NestedList = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(NestedList)

# 3. numpy array로 변환
Ndarrayd = np.array(NestedList) 
print(Ndarrayd)
print()

# 4. 각 원소에 1을 더하려면
result = Ndarrayd + 1 # 이것이 바로 브로드캐스팅! 
print('브로드캐스팅: ')
print(result)
print()

# NumPy에 구현된 메서드를 활용해 합이나 평균도 쉽게 구할 수 있습니다.
# 5. 전체 합 구하기
result = np.sum(Ndarrayd)
print('np.sum: ',result)
print()

# 6. 전체 평균 구하기
result = np.mean(Ndarrayd)
print('np.mean: ',result)
print()

# 7. 열의 평균 구하기
result = np.mean(Ndarrayd, axis=0)
print('열의 평균: ',result)

# 8. 행의 평균 구하기
result = np.mean(Ndarrayd, axis=1)
print('행의 평균: ',result)

# NumPy 장점
# 코어 부분이 C로 구현되어 동일한 연산을 하더라도 Python에 비해 속도가 빠름
# 라이브러리에 구현되어있는 함수들을 활용해 짧고 간결한 코드 작성 가능
# (효율적인 메모리 사용이 가능하도록 구현됨)

# 9. NumPy에서 Transpose 구현
x = np.array([[1,2],[3,4]], dtype = np.int8)
y = x.T

print(x)
print()

print(y)
print()

# 10. strides: 몇 칸을 건너 뛰는지에 대한 정보이다.
print(x.strides) 
print(y.strides)

# 11. 다차원 배열 생성
# 다차원 배열의 원소는 동일한 데이터 타입을 가져야 합니다.

# bool array 생성
boolArray = np.array([True, True, False, False])
print(boolArray)
print('boolArray.dtype: ',boolArray.dtype) 
print()

# int array 생성
intArray = np.array([[1,2],[3,4]])
print(intArray)
print('intArray.dtype: ',intArray.dtype)
print()

# unsigned int array 생성
uintArray = np.array([[1,2],[3,4]], dtype='uint')
print(uintArray)
print('uintArray.dtype: ',uintArray.dtype)
print()

# float array 생성
floatArray = np.array([[1.2, 3.14],[2.6, 5.6]])
print(floatArray)
print('floatArray.dtype: ',floatArray.dtype)
print()

# 아래 같은 경우는 data 손실이 발생한다.
intArray2 = np.array([[1.1, 2.2], [3.3, 4.4]], dtype='int')
print(intArray2)
print('intArray2.dtype: ',intArray2.dtype)
print()

# 12. 3차원 배열 만들기
three_d = np.array( [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]] )
print(three_d)
print(three_d.dtype)
print()

# 13. numpy.empty (초기화 하지 않았다.)
print(np.empty((2,3))) # 아무 값을 넣는다.
print()

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(np.empty_like(A))
print()

# 14. numpy.zeros (초기화를 0으로 해준다.)
B = np.zeros((2,3), dtype='int')
print(B)
print(B.dtype)
print()

C = np.zeros_like(A)
print(C)
print(C.dtype)
print()

# 15. numpy.ones
D = np.ones((2,3), dtype='int')
print(D)
print(D.dtype)
print()

# 16. numpy.identity
E = np.identity(2, dtype='int')
print(E)
print(E.dtype)
print()

# 17. numpy.eye
F = np.eye(3, dtype='int')
print(F)
print(E.dtype)
print()

G = np.eye(3,4,1)
print(G)
print(G.dtype)
print()

# 18. numpy.full
H = np.full((2,3),10)
print(H)
print(H.dtype)
print()

# 19. numpy.arange
# default value
# start = 0
# step = 1
J = np.arange(10)
print(J)
K = np.arange(start=1.0, stop=5.0, step=0.5)
print(K)
print()

# 20. numpy.linspace
L = np.linspace(2.0, 3.0, num=5)
print(L)
print()

# 21. numpy.amin (return the minimum of an array or minimun along an axis)
A_list = ([[1,2,3],[4,5,6],[7,8,9]])
A_np = np.array(A_list)
print(A_np)
print()

print('row minimum: ',np.amin(A_np, axis = 0))
print('col minimum: ',np.amin(A_np, axis = 1))
print('minimum: ', np.amin(A_np))

# 22. numpy.amax (최대값)
print('row maximun: ', np.amax(A_np, axis = 0))
print('col maximun:' , np.amax(A_np, axis = 1))
print('maximun: ', np.amax(A_np))

# 23. numpy.ptp (maximum - minimun)
print('ptp: ', np.ptp(A_np, axis = 0))
print('ptp: ', np.ptp(A_np, axis = 1))

# 24. numpy.median 
print('median: ', np.median(A_np, axis = 0))
print('median: ', np.median(A_np, axis = 1))

# 25. numpy.mean
print('mean: ', np.mean(A_np, axis = 0))
print('mean: ', np.mean(A_np, axis = 1))

# 26. numpy.var (분산)
print('var: ', np.var(A_np, axis = 0))
print('var: ', np.var(A_np, axis = 1))

# 27. numpy.std (표준편차)
print('std: ', np.std(A_np, axis = 0))
print('std: ', np.std(A_np, axis = 1))
print()
# 다차원 배열 다루기

# 28. 슬라이싱
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print('슬라이싱: ')
print(a[0:2, 0:4])
print()

# 29. 인덱싱
# 인덱싱을 통해 원소에 접근할 수 있다.
print(a[0][0]) # 원소에 접근하기
print(a[0,2]) # 원소에 접근하는 또 다른 방법

# 0행, 2행만 인덱싱
print(a[[0, 2], :])   # print(a[[0, 2], ])
# 0열, 1열, 3열만 인덱싱
print(a[:, [0,1,3]])
print()

print(a, a.shape, a.ndim)
print()
# 슬라이싱만 사용                    2 차원 !!! 
# 슬라이싱만 하면 차원이 유지되지만 인덱스를 사용하면 유지안됨
slicedRow = a[0:1, :]
print(slicedRow, slicedRow.shape, slicedRow.ndim)
print()

# 아래와 동일한 코드
# 인덱싱&슬라이싱 혼합 사용          1 차원 !!! 
# 슬라이싱만 하면 차원이 유지되지만 인덱스를 사용하면 유지안됨
indexedRow = a[0,:]
print(indexedRow, indexedRow.shape, indexedRow.ndim)

indexedRow = a[0]
print(indexedRow, indexedRow.shape, indexedRow.ndim)
print()
# 슬라이싱만 사용
slicedCol = a[:, 0:1]
print(slicedCol, slicedCol.shape, slicedCol.ndim)
print()
# 인덱싱&슬라이싱 혼합 사용
indexedCol = a[:, 0]
print(indexedCol, indexedCol.shape, indexedCol.ndim)
print()

# 30. 인덱싱과 슬라이싱의 또 다른 중요한 차이가 있다.
b = a[0,0] # 인덱싱 사용
b = 100
print(a)  # b 값을 바꿔도 a 행렬에는 영향을 주지 않는다.
print() 

c = a[1:3, 1:3]
# c[0, 0]은 a[1, 1]과 같은 데이터입니다.
c[0,0] = 100
print(a) # c값을 바꿨는데 a 행렬에 영향을 주었다.
print()
# 즉 슬라이싱은 값을 복사하는 것이 아니라 참조한다는 의미이다.

# 31. bool 배열 인덱싱
d = np.array([[1,2], [3,4], [5,6]])
bool_idx = (d>2)
print(d)
print()
print(bool_idx)
print()

# boolean indexing (data를 filtering 할 때 많이 쓰인다.)
print(d[bool_idx]) # 값이 참인 것만 출력된다.
print()

# 32. 정수 배열 인덱싱
a = np.array([[1,2], [3, 4], [5, 6]])
print(a[[0,1,2],[0,1,0]]) # [1, 4, 5] 가 출력!
# 위에서 본 정수 배열 인덱싱 예제는 다음과 동일합니다:
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # 출력 "[1 4 5]"

print(a[[0,0],[1,1]])
print()
# 위 예제는 다음과 동일합니다
# print(np.array([a[0, 1], a[0, 1]]))  # 출력 "[2 2]"

# 33. 전치행렬 (transpose)
x = np.array([[1,2], [3,4]])
y = x.T
print(x)
print(y)
print()

# 34. numpy.reshape

print('reshape')
print(np.arange(6).reshape((3,2))) # 2 dimension으로 변경된다.
print()

a = np.arange(6)
print(np.reshape(a,(2,3)))
print(np.reshape(a, 6)) # 1차원
print(np.reshape(a, (1,6))) # 2차원 (이렇게 써주도록 노력하자.)
print()
# 35. numpy.ravel 1 차원으로 만들어주는 함수
print(np.ravel(a))
print()

# 36. numpy.concatenate  연결
a = np.array([[1,2], [3,4]]) # 2D
b = np.array([[5,6]])

print(np.concatenate((a, b), axis=0))
print()

print(np.concatenate((a, b.T), axis=1)) # 행렬 계산을 생각해봐.
print()

# 37. trim_zeros (0을 제거하는 기능의 함수)
x = np.array((0, 0, 0, 1, 2, 3, 0, 2, 1, 0))
print(np.trim_zeros(x))
print()

# 38. 다차원 배열 연산
x = np.array([[1., 2.], 
              [3., 4.]])
y = np.array([[5., 6.],
              [7., 8.]])

print(x+y)
print()

print(np.add(x,y))
print()

print(x-y)
print()

print(np.subtract(x,y))
print()

print(x * y)
print(np.multiply(x, y))
print()

# 요소별 나눗셈; 둘 다 다음의 배열을 만듭니다

print(x / y)
print(np.divide(x, y))
print()
# 요소별 제곱근; 다음의 배열을 만듭니다

print(np.sqrt(x))
print()

# 39. Numpy에선 벡터의 내적, 벡터와 행렬의 곱, 
# 행렬곱을 위해 *대신 dot함수를 사용합니다.
# shape가 맞아야 연산이 이루어집니다.

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x)
print(y)
print()

v = np.array([9,10])
print(v)
w = np.array([11, 12])
print(w)

# 벡터의 내적;
print('벡터의 내적: ', v.dot(w))
print('벡터의 내적: ',np.dot(v, w))
print()
# 행렬과 벡터의 곱; 둘 다 결과는 dimension 1인 배열 [29 67]
print('행렬과 벡터의 곱: ', x.dot(v))
print('행렬과 벡터의 곱: ', np.dot(x, v))
print()
# 행렬곱; 둘 다 결과는 dimension 2인 배열
# [[19 22]
#  [43 50]]
print('행렬곱')
print(x.dot(y))
print()

print('행렬곱')
print(np.dot(x, y))
print()

# 40. NumPy 고급 기능
# 브로트캐스팅은 Numpy에서 shape가 다른 배열 간에도
# 산술 연산이 가능하게 하는 메커니즘입니다.

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) # 다차원 배열
v = np.array([1, 0, 1]) # 벡터
# x와 v는 더하거나 뺄 수 없다.
print(x)
print()
print(v)
print()
print(x+v) # 그러나 x와v가 더 할 수 없음에도 불구하고
           # tile 과정을 numpy가 알아서 해준 경우이다.
print()

# v의 복사본 4개를 위로 차곡차곡 쌓은 것이 vv
vv = np.tile(v,(4,1))
print(vv)
print(vv.shape)
print()

print(vv+x)
print()

print(vv+x+1) # 1을 더할 때, 브로드캐스팅 된 것이다.
print()

# 브로드캐스팅의 예
v = np.array([1,2,3])  # v의 shape는 (3,)
w = np.array([4,5])    # w의 shape는 (2,)
x = np.array([[1,2,3], 
              [4,5,6]])

print( v + x)
print()

# transpose를 이용
xt = x.T
print((xt + w).T) # 다시한번 transpose를 해준다.




