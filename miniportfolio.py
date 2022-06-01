print("""1. 아메리카노 (hot): 2,500원
2. 아이스 아메리카노 : 3,000원
3. 핫 초코 : 4,000원""")

menuList = [2500, 3000, 4000]
a = int(input("메뉴를 선택해 주세요. (숫자로 입력해주세요) "))
print()

if (0 < a < 4):
    num = int(input("선택하신 메뉴의 수량을 선택해주세요. (숫자로 입력해주세요.) "))
    print()
    print("총 결제하실 금액은", menuList[a-1]*num, "원입니다.")
else:
    print("메뉴를 잘못 입력하셨습니다. 다시 한 번 확인해주세요")


menuChoice = input("맞을 경우 y를, 아닐 경우 n을 눌러주세요.")
print()
if menuChoice == "y" or menuChoice == "Y":
    print("결제가 완료되었습니다.")
else:
    print("결제에 실패하였습니다.")
