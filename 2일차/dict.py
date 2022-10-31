'''
p.216,217
딕셔너리
'''

# info = {"name":"홍길동", "age":20}
# print(info['name']) # 파이썬은 이렇게 해야함. 대괄호 안에 키를 넣음
# print(info['age']) 

info = {}
#이름입력받기
info["name"] = input("이름 입력 : ")
#나이입력
info["age"] = input("나이 입력 : ")
#주소입력
info["addr"] = input("주소 입력 : ")

#info 출력
for key in info:
    print(f"\n{key}\t{info[key]}")

#주소 지우기
# del info["addr"]
# print(info)