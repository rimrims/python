'''
filename : list3.py
리스트 삭제
'''
members=[
    {'name':'김','age':20,'addr':'서울'},
    {'name':'송','age':32,'addr':'대구'},
    {'name':'최','age':27,'addr':'구미'}
]

#이름 검색 후 해당하는 사람의 이름과 주소 출력
name = input("검색할 이름 입력 : ")
for i in range(len(members)):
    if name in members[i]["name"]:
        print(f'{members[i]["name"]} \t {members[i]["addr"]}')
        del members[i] # 한 명 삭제되면 members배열 2개 됨. indexError
        break   #for문 빠져나오기

print(members)