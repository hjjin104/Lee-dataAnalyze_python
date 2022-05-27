# # Q1 학점계산기

# AA = 4.5
# A = 4.0
# BB = 3.5
# B = 3.0
# CC = 2.5
# C = 2.0
# F = 0

# writing = 3
# math = 3
# English = 2
# computing = 3

# res = writing*A + math*C + English*BB + computing*AA
# total_Score = writing+math+English+computing

# avgScore = res/total_Score

# print(avgScore)
# print()

# # Q2 십의 자리 구하기
# a = input("하나의 숫자를 입력해주세요. (단, 입력하는 숫자는 무조건 두 자리 이상의 자연수를 입력해주세요.)")
# print(a[0])
# print()


# Q3 주민등록번호 가리기
idNum = "951004-2345678"
privateIdNum = idNum[7::]
print(privateIdNum.replace(privateIdNum, '*******'))

# # Q4 호텔 예약 관리하기
# bookList = [103, 205, 405]
# newBooking = [107, 203, 304, 507]

# finalBooking = bookList+newBooking
# finalBooking.sort()
# # finalBooking = bookList.extend(newBooking)
# print("현재 예약된 방은 ", finalBooking, "입니다.")
# print()

# finalBooking.remove(205)
# finalBooking.remove(304)

# print("현재 예약된 방은 ", finalBooking, "입니다.")
# print()


# # Q5키순으로 줄 세우기
# childern = [175.3, 146, 184, 160, 167]
# childern.sort()
# print("키 작은 순서대로 정렬하기: ", childern)
