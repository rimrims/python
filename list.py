'''
list == array
배열에 요소 추가, 삭제, 조회, 변경
'''
arr = ['김','이','박','옹']

#마지막에 최씨 추가
arr.append('최')

#맨 처음에 강씨 추가
arr.insert(0,'강')

#김씨 빼기 - del함수 이용
del arr[1] #범위를 지정하고 싶을때 : [시작인덱스:끝인덱스]

#박 - remove함수이용해서 지우기
arr.remove('박')

print(arr)