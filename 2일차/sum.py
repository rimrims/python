score = [10,50,100]

total = 0
for s in score:
    total += s

print('합계',total)

#최소 최댓값 구할 때는 초기값을 0이 아닌 배열의 첫번째 값으로!
maxScore = score[0] #배열 값이 음수인 경우 대비
minScore = score[0] # 초기값을 0으로 하면 0으로 출력함.

for s in score:
    if maxScore < s:
        maxScore = s
    if minScore > s:
        minScore = s

print('최댓값',maxScore)
print('최솟값',minScore)