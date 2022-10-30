# A = input("0<A")
# B = input("B<10")
# sum = int(A)
# print(sum)

#입력
s = input()
#문자를 자른다(배열에 넣음)
score = s.split(" ")
#정수형 변환
A = int(score[0])
B = int(score[1])
#합계
# total = A*B
#출력
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)