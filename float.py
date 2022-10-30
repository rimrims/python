'''
filename : float.py
실수값 2개를 입력받아서 합계 계산하고 출력하는 프로그램
'''
# 입력
s = input()
#문자 자르기
flt1,flt2 = s.split(" ")
# 실수형으로 변환
flt1 = float(flt1)
flt2 = float(flt2)
# 합계
total = flt1+flt2
# 출력
print(total)