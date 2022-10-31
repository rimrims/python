'''
filename:range.py
특정한 횟수만큼 반복
'''

#1~10
# for i in range(1,11):
#     print(i)

#홀수값만
# for i in range(1,11,2):
#     print(i) # 1 3 5 7 9

#짝수값만
# for i in range(0,11,2):
#     print(i)

# for i in range(1,6):
#     print("*"*i)

# for i in range(5,0,-1):
#     print("*"*i)

# for i in range(11,0,-2):
#     print("*"*i)
# ===========================================================
# 공백 만들어서 별 찍기.(쭉 적어서 규칙 찾고 식 세우기)
# for i in range(11,0,-2):
#     print(" "*(11-i//2),"*"*i)
'''
11 - 0  (11-i)//2 
9 - 1
7 - 2
5 - 3
'''
# ===========================================================
# n=int(input())
# for i in range(1,n+1):
#     print((n-i)*" ","*"*i) # 0부터 하면 공백으로 찍힘.

''' 공백은 어떻게 식 세울까?
i=1 공백=4 / 5-1=4
i=2 공백=3 / 5-2=3
i=3 공백=2 / 5-3=2 --> n-i=공백 이라는 식 세워짐
'''

n=int(input())
# for i in range(1,n+1):
#     #공백출력
#     for j in range(n-i):
#         print(" ",end="") # end가 없으면 별 하나 찍고 줄바꿔짐.
#     #별출력
#     for j in range(i):
#         print("*",end="")
#     print()

output=""
for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        output += " "
    #별출력
    for j in range(i):
        output += "*"
    output += '\n'
print(output)