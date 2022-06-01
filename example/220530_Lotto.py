import random

lottoNum = []

while True:
    r = random.randint(1, 45)
    lottoNum.append(r)
    if len(lottoNum) == 6:
        break
print(lottoNum)
