'''
filename : string_index.py
문자열 인덱싱(자르기)
'''

#인덱싱(p95)
a = "960114"

# 한글자만 추출(p97)
print("첫번째 문자", a[0]) # js도 가능
print("마지막 문자", a[-1])
print("출생년도", a[:2])
print("출생월", a[2:4])
print("출생일", a[-2:])
print("indexerror", a[7])

