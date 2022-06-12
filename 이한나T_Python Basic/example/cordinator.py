temp = int(input("오늘 기온을 입력해주세요: "))

print("오늘 기온은", str(temp)+"도 입니다.")
if temp < 24:
    print("긴바지를 입으세요")
    if temp < 10:
        print("외투도 입는 게 좋겠네요.")
else:
    print("반바지를 입으세요")
