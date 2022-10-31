'''
반복문 맹연습!!!!!!!!!!!!!!!!!!!!!!!
'''

#list는 인덱스로 접근 dictionary는 key로 접근

#==================================================list
from re import S


names = ['김','이','박']

print("list===")  
for obj in names: # 내용 자체를 가지고 옴
    print(obj) #김 이 박

print("list range===")
for idx in range(len(names)):  # 인덱스(방)을 가져옴
    print(names[idx])

#====================================================dictionary
dict = {'no':100, 'username':'user1', 'salary':2000}

print("dict=====")
for key in dict:
    print(key,dict[key])

print("dict items=====") #p.256
for key,value in dict.items(): # 바로 위 것과 같음.
    print(key,value)

#=================================================list안의 dictionary
users = [ {'no':100, 'username':'user1', 'salary':2000},
          {'no':101, 'username':'user1', 'salary':1000},
          {'no':102, 'username':'user1', 'salary':1500}]

print("list dict=====")
for obj in users:
    print(obj["username"])

print('list dict range=====')
for idx in range(len(users)):
    print(users[idx]["username"])

#급여 합계 출력
total = 0
for sal in users:
     total += sal["salary"]
print(total)

#최대급여와 최소급여
maxSalary = users[0]["salary"]
minSalary = users[0]["salary"]

for s in users:
    if maxSalary < s['salary']:
        maxSalary = s['salary']
    if minSalary > s['salary']:
        minSalary = s['salary']
'''
for s in range(len(users)):
    if users[s]['salary'] < maxSalary:

'''

print("최소",minSalary)
print("최대",maxSalary)