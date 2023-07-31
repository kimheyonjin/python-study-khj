### 딕셔너리 자료형 ###
# 키와 값의 쌍을 항목으로 가지는 자료형
# 중괄호{}로 표현, 각 항목은 클론(:)으로 키와 값을 구분
# 키를 통해 요솟값을 빠르게 검색 가능

#변경 가능 0, 키는 중복 x 값은 중복 0

#1.  dictionary 생성
dict1 = {} # 빈 딕셔너리
dict2 = {'name': 'Jun Gook', 'age': 29, 'city':'Busan'}
dict3 = dict(name='JunGook', 'age': 29, 'city':'Busan')

#2. 키를 사용해 값에 접근
dict = {'name': 'Jun Gook', 'age': 29, 'city':'Busan'}
print(dict['name'])#출력 Jun Gook

#3  dictionary에 항목 추가/ 수정/ 삭제
(dict['age']) = 29# 기존 키의 값을 수정
dict['country'] = 'Korea'
print(dict)

del dict['country'] # 키 'country'의 항목 삭제
print(dict)
#파이썬 교재 p46 딕셔너리 내장 함수