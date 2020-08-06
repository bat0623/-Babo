# #quiz1
# station = "사당"
# print(station +"행 열차가 들어오고 있습니다.")

# # quiz2
# from random import *
# date = randint(4,28)
# print ("오프라인 스터디 모임 날짜는 매월" + str(date) +"일")

# #quiz3
# url = "http://naver.com"
# url = "http://daum.com"
# url = "http://youtube.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url,password))

# # quiz4
# from random import *
# users = range(1,21)
# users = list(users)

# print(users)
# shuffle(users)
# print(users)


# winners = sample(users, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다. --")

# # quiz5
# from random import *
# cnt = 0# 총 탑승 승객
# for i in range(1,51): # 50명의 승객
#     time = randrange(5,51)# 5분~ 50분 소요시간
#     if 5<= time and time <= 15: # 5~15분 이내의 손님, 답승 승객수 증가처리
#         print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
# print("총 탑승 승객 :{0}분 ".format(cnt))

# quiz6

# def std_weight(height, gender):# 키 m 단위
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 164 # cm 단위
# gender = "여성"
# weight = round(std_weight(height/100,gender),2)
# print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height,gender,weight))
