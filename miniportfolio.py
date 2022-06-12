<<<<<<< HEAD
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
=======
# print("""==============Menu==============
# 1. 아메리카노 (hot): 2,500원
# 2. 아이스 아메리카노 : 3,000원
# 3. 핫 초코 : 4,000원
# """)

# menuList = [2500, 3000, 4000]

# print()

# while True:
#     a = int(input("메뉴 번호를 선택해 주세요. "))
#     if (0 < a < 4):
#         num = int(input("선택하신 메뉴의 수량을 선택해주세요. "))
#         print()
#         print("총 결제하실 금액은", menuList[a-1]*num, "원입니다.")
#         print()
#         menuChoice = input("맞을 경우 y를, 아닐 경우 n을 눌러주세요. ")
#         print()
#         if menuChoice == "y" or menuChoice == "Y":
#             print("결제가 완료되었습니다.")
#         else:
#             print("결제에 실패하였습니다.")
#         break
#     else:
#         print("메뉴를 잘못 입력하셨습니다. 다시 한 번 확인해주세요")


# hot_ame = 2500
# ice_ame = 3000
# hot_cho = 4000
# print("MENU")
# print("뜨아: %d원" % hot_ame)
# print("아아: %d원" % ice_ame)
# print("핫초코: %d원" % hot_cho)

# li = ["뜨아", "아아", "핫초코"]

# order = input("메뉴를 선택하세요: ")
# qtt = int(input("수량을 선택하세요: "))

# for x in li:
#     if order == "뜨아":
#         print("결제 금액: ", hot_ame * qtt, "원, 맞으면 y / 틀리면 n 를 눌러주세요")
#     if order == "아아":
#         print("결제 금액: ", ice_ame * qtt, "원, 맞으면 y / 틀리면 n 를 눌러주세요")
#     if order == "핫초코":
#         print("결제 금액: ", hot_cho * qtt, "원, 맞으면 y / 틀리면 n 를 눌러주세요")


# sw = input("눌러")

# if sw == "y":
#     print("결제가 완료되었습니다")
# if sw == "n":
#     print("결제가 실패하였습니다")


print("""==============Menu==============
1. 아메리카노 (hot): 2,500원
2. 아이스 아메리카노 : 3,000원
3. 핫 초코 : 4,000원
""")

menuList = [2500, 3000, 4000]

print()

while True:
    a = int(input("메뉴 번호를 선택해 주세요. "))
    if (0 < a < 4):
        num = int(input("선택하신 메뉴의 수량을 선택해주세요. "))
        print()
        print("총 결제하실 금액은", menuList[a-1]*num+"원입니다.")
        print()
        menuChoice = input("맞을 경우 y를, 아닐 경우 n을 눌러주세요. ")
        print()
        if menuChoice == "y" or menuChoice == "Y":
            print("결제가 완료되었습니다.")
            break
        else:
            print("결제에 실패하였습니다.")

    else:
        print("메뉴를 잘못 입력하셨습니다. 다시 한 번 확인해주세요")
>>>>>>> f03759c (Jupyter file to python file)
