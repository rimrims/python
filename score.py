'''
점수 3개를 입력받아서 합계를 구하는 프로그램
수도코드 : 말로 짜는 코드(로직 짜서 한글로 쭉 써놓음)
'''
#입력
s = input("점수 입력 : ")
#문자를 자른다(배열에 넣음) # 여러개의 데이터 받았으므로 잘라줘야함
score = s.split(" ")
#정수형 변환
kor = int(score[0])
eng = int(score[1])
mat = int(score[2])
#합계
total = kor+eng+mat
#평균
aver = total/3
#출력 : 평균이 90이상이면 수, 80이상 우,70이상 미,나머지 양
if aver>=90:
    print("수")
elif aver>=80:
    print("우")
elif aver>=70:
    print("미")
else:
    print("양")