age = int(input("나이를 입력하세요. "))
# print(age//10)

# input 값 45, 25인 경우 print 안 됨
# List version
# _10s = ["어벤져스", "뮬란"]
# _20_30s = ["뮬란", "테넷", "오!문희"]
# _40_50s = ["테넷"]
# _60s = ["오!문희"]
# if age // 10 == 0 | age // 10 == 1:
#     print(_10s)
# if age // 10 == 2 | age // 10 == 3:
#     print(_20_30s)
# if age // 10 == 4 | age // 10 == 5:
#     print(_40_50s)
# if age // 10 > 5:
#     print(_60s)

# Dictionary Version
recommend_movies = {'10대': ["에벤져스", "뮬란"],
                    "2030": ["뮬란", "테넷", "오!문희"],
                    "4050": ["테넷"],
                    "60": ["오!문희"]
                    }

if age // 10 < 2:
    print(recommend_movies['10대'])
if 1 < age // 10 < 4:
    print(recommend_movies['2030'])
if 3 < age // 10 < 6:
    print(recommend_movies['4050'])
if age // 10 > 5:
    print(recommend_movies['60'])
