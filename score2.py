'''
점수 3개를 입력받아서 합계를 구하는 프로그램
수도코드 : 말로 짜는 코드(로직 짜서 한글로 쭉 써놓음)
'''
#입력
# s = input("점수 입력 : ")

#문자를 자른다(배열에 넣음)
kor,eng,mat = input().strip().split(" ") #각각의 변수에 값을 넣는게 가능(파이썬만)
                                            # 앞뒤 공백 없애줌. strip없으면 공백있게 입력하면 오류
#정수형 변환
kor = int(kor)
eng = int(eng)
mat = int(mat)
#합계
total = kor+eng+mat
#평균
aver = total/3
#출력 (p136)
print("국어:{} 영어:{} 수학:{} \n 합계:{} \n 평균:{}".format(kor,eng,mat,total,aver)) #국어: 영어: 수학: 합계:
print(f"국어:{kor} 영어:{eng} 수학:{mat} \n 합계:{total} \n 평균:{aver}") # f문자열로 표현