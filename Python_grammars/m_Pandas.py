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
print()

# 9. Pandas Importing/Exporting
# Importing 함수의 경우 pd.read 형태를 가지며
# Exporting 함수의 경우 df.to 형태를 가집니다.
print(dataf1)
print()

# exproting 방식 (json 형식)
json_data = dataf1.to_json()
print(json_data) 
print()

# print(dataf1.to_html())

# importing 방식
print(pd.read_json(json_data))
print()

# 10. CSV 
# 파일다운로드 받기 ( file importing )
df_iris_sample = pd.read_csv('iris_sample.csv') 
print(df_iris_sample)
print()

# csv뿐만 아니라 tsv, txt도 read_csv()파일을 
# 통해 읽어올 수 있습니다.

# file exporting
print(df_iris_sample.head()) # 첫 5행만 가져와라.
print()
print(df_iris_sample.tail()) # 마지막 5행만 가져와라.
print()

df_iris_sample_2 = df_iris_sample.head()
df_iris_sample_2.to_csv('iris_sample_2.csv',index = False) # file exporting
# Unnamed: 0 라는 열이 들어가 있습니다. 
# 이는 to_csv()시 index도 함께 파일에 저장되기에 생기는 문제입니다.
print(pd.read_csv('iris_sample_2.csv')) 
print()

# 이번에는 excel 파일을 importing하거나 exporting 해본다.
# 기본적으로 read_excel()은 첫번째 시트를 가져옵니다. 
df_rank_sample1 = pd.read_excel('성적표.xlsx', sheet_name=0)

# 두 번째 시트를 가져오려면 sheet_name 파라메터에 
df_rank_sample2 = pd.read_excel('성적표.xlsx', sheet_name=1)

print(df_rank_sample1)
print()

print(df_rank_sample2)
print()

df_sheet2 = pd.read_excel('성적표.xlsx', sheet_name='Sheet2')
df_sheet2.to_excel('to_excel.xlsx', sheet_name='kingdom', index=False)
print(pd.read_excel('to_excel.xlsx'))
print()

# 11. 데이터베이스 연결 mysql에 연결
#import sqlalchemy

#user = "anonymous"
#host = "ensembldb.ensembl.org"
#port = 3337
#database = "ailuropoda_melanoleuca_core_79_1"

#url = f"mysql+mysqlconnector://{user}@{host}:{port}/{database}"
# url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

# pip install -U chatterbot
# pip install sqlalchemy 
#connection = sqlalchemy.create_engine(url)
#connect_sql = pd.read_sql("select * from analysis limit 3", connection)
#print(connect_sql)
#print()

# 12. 데이터를 다루는 기술에 대해 배운다.
print(dataf1)
print()

print(dataf1['Country'])
print()

print(dataf1[['Country', 'Population']])
print()

# 이제 슬라이싱에 대해 다룬다
print(dataf1[0:2]) # 0 행, 1 행 만 가져온다.
print()

print(dataf2)
print()

# label 슬라이싱. 'cc' 포함
print(dataf2['aa':'cc'])
print()

# 13. loc (Label based indexing)
#     iloc (Positional indexing)

# 위치를 통한 인덱싱
print(dataf1.iloc[0,0])
print()
# 위치를 통한 인덱싱
print(dataf1.iat[0,0])
print()

# 라벨을 통한 인덱싱
print(dataf1.loc[0,'Country'])
print()
# 라벨을 통한 인덱싱
print(dataf1.at[0,'Country'])
print()

# 14. 슬라이싱 (연속된 값을 가져오는 것이다.)
print(dataf1.iloc[0:1,0:2]) # 위치를 통한 슬라이싱 (끝은 미포함)
print()

print(dataf1.loc[0:1, 'Country':'Capital']) # 라벨을 통한 슬라이싱 (끝 포함))
print()

# 15. 블리언 인덱싱 (필터링)
print(dataf1.loc[:,'Population'] > 200000000)
print()
print(dataf1[dataf1['Population'] > 200000000])
print()
