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

