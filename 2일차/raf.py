users = [ {'no':100, 'username':'user1', 'salary':2000},
          {'no':101, 'username':'user1', 'salary':1000},
          {'no':102, 'username':'user1', 'salary':1500}]


while True:
    
    print("1. 추가 2. 삭제 3. 조회 4.전체조회 5.종료")
    s = int(input("메뉴선택: "))
    
    if s == 1:
        info = {}
        info["no"] = int(input("회원번호: "))
        info["username"] = input("이름: ")
        info["salary"] = int(input("봉급: "))
        users.append(info)
        
    elif s == 2:
        num = int(input("삭제할 회원번호: "))
        # for i in range(len(users)):
        #     if num == users[i]["no"]:
        #         del users[i]
        
        idx = 0
        for mem in users:
            if num == mem["no"]:
                del users[idx]
        idx += 1
        
    elif s == 3:
        num = int(input("조회할 회원번호 : "))
        for i in users:
            if num == i["no"]:
                print(i["username"],i["salary"])

    elif s == 4:
        for i in users:
            print(i["username"],i["salary"])
            
    elif s == 5:
        print("종료")
        break
    
print("종료")
