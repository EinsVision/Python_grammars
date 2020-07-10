import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Pandas는 다음과 같은 특징을 같습니다.

# NumPy를 내부적으로 활용함(NumPy의 특징을 그대로 가짐)
# 데이터분석에 특화된 데이터 구조 제공
# 다양한 데이터 분석 함수 제공
# 데이터베이스에 쉽게 연결 가능

# help(pd.DataFrame) # help는 이렇게 사용하면 된다.

# 1. Pandas 데이터 구조
# Series (1차원 배열 자료 구조)
# DataFrame (2차원 자료 구조 / 엑셀시트와 비슷) 
s = pd.Series([8,-6, 3, 5]) # 인덱스 없이 생성
print(s)
print()
print(type(s))
print()

# Pandas는 인덱스를 넣고 생성할 수 있다.
ss = pd.Series([8, -6, 3, 5], index=['a', 'b', 'c', 'd'])
print(ss)
print()
print(type(ss))
print()

# Series는 index와 value를 가진다.
print(ss.index)
print()
print(ss.values)
print()

# 2. 인덱싱 ( 값을 가져오는 행위 )
# Series는 요소는 index명 또는 index의 순서를 통해 
# 인덱싱할 수 있습니다.

# index명으로 조회
print(ss['a'])
# index순서로 조회
print(ss[0])
print()
# python dictionary와 공통점, 차이점 
pop_dict =  {'Germany': 81.3,  # key, data 
            'Belgium': 11.3, 
            'France': 64.3, 
            'United Kingdom': 64.9, 
            'Netherlands': 16.9}

print(pop_dict)
print(type(pop_dict))    # <class 'dict'>
print()

# python의 dictionary로 Series 생성
population = pd.Series(pop_dict)
print(population)
print(type(population))  # <class 'pandas.core.series.Series'>
print()

# dictionary key 값 가져오기
print(pop_dict['Germany'])

# Series의 index 값 가져오기
print(population['Germany'])
print()

# 3. 딕셔너리와 Series의 차이점은, 
# 딕셔너리의 Key는 순서가 없고 
# pandas Series의 index는 순서가 있다는 점입니다. 

# print(pop_dict[2]) # dictionary는 순서가 없다.
print(population[2]) # dictionary와 Series의 차이
print()

# Series는 딕셔너리와 다르게 아래와 같은 연산이 가능합니다.
print(population*1000) # elementwise 연산이 가능하다.
# NumPy에서는 브로드캐스팅이라고 한다.
# print(pop_dict*1000) # 불가능하다.
print()

# 4. DataFrame
# 2차원 데이터 구조
# 일반적으로 df로 이름 붙임
# 엑셀 스프레드시트, 데이터베이스등과 동일한 2차원 구조
# 가장 많이 활용하게될 구조
# Series가 합쳐진 형태

# 중첩된 리스트를 통한 데이터 생성
# 각 행을 리스트로 만들어야 함
data = [['Belgium', 'Brussels', 11190846],
        ['India', 'New Delhi', 1303171035],
        ['Brazil', 'Brasília', 207847528]]

# 이렇게 넣으면 columns을 지정할 수 있다. 
dataf = pd.DataFrame(data, columns=['Country', 'Capital', 
                                    'Population'])
print(dataf)
print()

# 다음은 dictionary로 DataFrame을 만드는 경우이다.
# columns 설정하지 않아도 된다.
data1 = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]}

dataf1 = pd.DataFrame(data1)
print(dataf1)
print()

dataf2 = pd.DataFrame(data1, index=['aa','bb','cc'])
print(dataf2)
print()

print(dataf2['Country'])
print(type(dataf2['Country']))
print()

# 5. DataFrame의 속성 (index, columns, dtypes, values)
print(dataf2.index)
print()
print(dataf2.columns)
print()
print(dataf2.dtypes)
print()
print(dataf2.values)
print()

print(dataf2.info()) # DataFrame의 속성을 한번에 검사하는 방법
print()

# 6, 특정한 칼럼을 index로 사용할수도 있습니다.
df_index_with_country = dataf2.set_index('Country')
print(df_index_with_country)
print()

# 하나의 인덱스만 가능한것은 아닙니다. 
# DataFrame은 여러개의 인덱스를 가질 수 있습니다.
df_index_couple = dataf2.set_index(['Country', 'Capital'])
print(df_index_couple)
print()

# 인덱싱 (여러개의 인덱스에서 값을 가져올 때)
print(df_index_couple.loc[['Belgium', 'Brussels']])
print()

# 7. Dataframe의 column은 어떤 데이터타입일까
s_1 = pd.Series([1,2,3,4], index=['A','B','C','D'])
s_2 = pd.Series([5,6,7,8], index=['A','B','C','D'])
s_3 = pd.Series([9,10,11,12], index=['A','B','C','D'])

data = {'col1':s_1,
        'col2':s_2,
        'col3':s_3 }

df_4 = pd.DataFrame(data, index=['A','B','C','D'])
print(df_4)
print()

# DataFrame도 elementwise 연산이 가능하다.
print(dataf2['Population'])
print()

print(dataf2['Population']/1000)
print()

print(dataf2['Country']+dataf2['Capital']) # 문자열도 더할 수 있음
print()

# 8. NumPy ndarray와 비교 
# Series간 연산을 하는 경우, index를 기반으로 이루어집니다.
print(ss)
s1 = ss[['a','b']]
s2 = ss[['b','c']]
print(s1+s2) 
# a     NaN
# b   -12.0
# c     NaN
print()

# 연습문제
# df_index_with_country이 데이터로 주어졌을때 
# 각 국가의 수도 인구는 벨기에 수도 인구 대비 몇 배인지 구하세요.
print(df_index_with_country)
print()

print(df_index_with_country['Population'])
Belgium = df_index_with_country['Population']['Belgium']
print(Belgium)
print()

India = df_index_with_country['Population']['India']
print(India)
print()
print(India/Belgium)

