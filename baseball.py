'''
filename : baseball
숫자야구게임
'''
#컴퓨터 난수 3개
from random import randint
import sys


c1 = randint(1,9)
c2 = randint(1,9)
c3 = randint(1,9)

print(c1,c2,c3)

cnt = 0 #게임시도횟수
s = 0 #점수 리셋

while s < 3 and cnt < 5: # 조건이 거짓이 되면 끝남.
    cnt += 1
    #게이머가 값 입력
    n1,n2,n3=input().split(' ')

    #정수형 변환
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)

    s=0
    b=0 #초기화
        
    #스트라이크 수 계산
    if c1 == n1:
        s += 1
    if c2 == n2:
        s += 1
    if c3 == n3:
        s += 1


    #볼 개수 계산
    if c1 == n2 or c1 == n3:
        b += 1
    if c2 == n1 or c2 == n3:
        b += 1
    if c3 == n1 or c3 == n2:
        b += 1

    print(f'스트라이크:{s} ball:{b}')

if s == 3:
    print("축하")
    if cnt <= 3:
        print("천재")
    elif cnt == 4:
        print("우수")
    else:
        print("보통")
if s != 3 :
    print("게임 종료")
    

# 스트라이크 3이면 "축하"
    # 시도횟수 3번만에 맞추면 "천재"
    # 시도횟수 4번 -> "우수"
    # 아니면 "보통"
#스트라이크 3 아니면 "게임 종료"