'''
filename : continue.py
'''
total = 0
score=[10,5,20,3,25]
for s in score:
    if s > 10:
        total += s
        print(s)

total = 0
for s in score:
    if s <= 10:
        continue #for문으로 돌아감
    total += s
    print(s)