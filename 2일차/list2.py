'''
filename : list2.py
리스트 조회
'''
members=[
    {'name':'김','age':20,'addr':'서울'},
    {'name':'송','age':32,'addr':'대구'},
    {'name':'최','age':27,'addr':'구미'}
]

#전체출력(이름과 주소 출력)
# for mem in members:
    # print(mem["name"],mem["addr"])

#나이 검색 후 해당하는 사람의 이름과 주소만 출력.
    # age = int(input("검색할 나이 입력 : "))
    # if mem["age"] == age :
    #     print(f'{mem["name"]} \t {mem["addr"]}')

#이름 검색 후 해당하는 사람의 이름과 주소 출력
name = input("검색할 이름 입력 : ")
for mem in members:
    if name in mem["name"]: # p.145
  # if mem["name"].find(name) >= 0 :  # (=js indexof)find함수에서 0 이상의 값 나오면 이름 찾은 것
        print(f'{mem["name"]} \t {mem["addr"]}')