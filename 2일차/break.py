'''
filename : break.py
'''

users = [ {'no':100, 'username':'user1', 'salary':2000},
          {'no':101, 'username':'user1', 'salary':1000},
          {'no':102, 'username':'user1', 'salary':1500}]

while True:
    print("1. 추가 2. 삭제 3. 조회 4.전체조회 5.종료")
    no = int(input("메뉴선택 : "))
    if no == 1:
        print("추가")
        info={}
        info["no"]=int(input("회원번호 : "))
        info["username"]=input("회원이름 : ")
        info["salary"]=int(input("봉급 : "))
        users.append(info)
        
    elif no == 2:
        print("삭제")
        userNo = int(input("삭제할 번호 입력 : "))
        # for i in range(len(users)):
        #     if userNo == users[i]["no"]:
        #         del users[i]
        
        idx = 0
        for i in users:
            if i["no"] == userNo:
                del users[idx]
                break
            idx += 1 # if문이 거짓이면 idx값에 +1되면서 배열값 맞아들어감.

    elif no == 3:
        print("조회")
        #번호 입력
        userNo = int(input("조회할 번호 입력 : "))
        #username과 salary 출력
        for user in users:
            if userNo == user["no"]: #리스트,문자열은 in으로 비교, 다른것은 == 로 비교
                print(user["username"],user["salary"])

    elif no == 4:
        print("전체조회")
        #username, 급여
        for user in users:
            print(user["username"],user["salary"])

    elif no == 5: 
        print("종료")
        break

print("the end")