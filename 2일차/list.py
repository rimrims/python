'''
리스트 다루기(배열)
'''
from os import lseek


# list_a = ['hello', 10, True]
# print(list_a[0])
# print(list_a[0][0]) # h 출력 (리스트 첫번째의 첫번째 글자)

list = []             #배열

for i in range(3):        #세 명의 회원을 등록하려면 세 번 반복
    info = {}        #딕셔너리(객체)

    #이름입력받기
    info["name"] = input("이름 입력 : ")
    #나이입력
    info["age"] = input("나이 입력 : ")
    #주소입력
    info["addr"] = input("주소 입력 : ")
    #리스트에 추가
    list.append(info)   #info 딕셔너리를 list(배열)에 추가

# print(list)

#list에서 이름과 나이 출력
for member in list:
    print(f'{member["name"]} \t {member["age"]}')
