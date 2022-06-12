# print(birthplace)
# print(type(birthplace))

while True:
    Idinput = input("주민등록번호를 (-) 빼고 입력하세요: ")
    if len(Idinput) != 13:
        print("잘못된 주민번호입니다. 다시 한 번 확인해주세요.")
    else:
        birthplace = int(Idinput[7:9])
        if birthplace < 9:
            print("서울")
        elif 8 < birthplace < 13:
            print("부산")
        elif 12 < birthplace < 16:
            print("인천")
        elif 15 < birthplace < 26:
            print("경기")
        elif 25 < birthplace < 35:
            print("강원")
        elif 34 < birthplace < 48:
            print("충청")
        elif 47 < birthplace < 67:
            print("전라")
        elif 66 < birthplace < 92:
            print("경상")
        elif 92 < birthplace < 96:
            print("제주")
        else:
            print("지역번호가 잘못 입력된 주민번호입니다.")
        break
# if birthplace == 00 or 01 |birthplace == 02|birthplace == 03 |birthplace == 04 |birthplace == 05 |birthplace == 06 | birthplace == 07 | birthplace == 08:
# print("서울")
# if birthplace == 09 |birthplace == 10 |birthplace == 11:
