'''
오븐시계 계산
'''
# 현재시간 입력받음(시, 분)
h,m = input().split(' ')
# 요리시간 입력받음()
s = input()
# 정수형 타입변환
h =int(h) # 자바는 변수명 달라야 함
m =int(m)
s =int(s)
# 시간 - 현재시간을 60으로 나눈 몫 => 시에 더함 / 나머지 => 분에 더함
h += (s//60)
m += (s%60)
#       요리시간 분을 60으로 나눈 몫 -> 시에 더함 / 나머지 -> 분에 저장.
h += (m//60)
m = m%60
# 출력
print(h,m)
#시간이 24시라면 0시로 변경
