

# #문자열 처리함수

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))

# index = python.index("n")
# print(index)
# index = python.index("n",index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("Java"))

# print (python.count("n"))

# #문자열 포맷

# #방법 1
# print("나는 %d 살입니다.", % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# print("나는 %s 살입니다.", % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간" ))

# #방법 2
# print("나는 {} 살입니다.".format(20))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color= "흰"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "흰", age= 20))

# #방법 4
# age = 20
# color = "흰"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# #탈출 문자

# #\n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# #\" \' : 문자내에서 따음표
# #저는 "바보"입니다.
# print('저는 "바보"입니다.') 
# print("저는 \"바보\"입니다.")
# print("저는 \'바보\'입니다.")

# #\\ : 문장 내에서 \
# print("d:\\Github\\-Babo\\mission\\nado_coding_practice.py")

# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# #\b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# #\t : 탭(tab)
# print("Red\tApple")

# #리스트 []

# subway = [10,20,30]
# print(subway)
# subway = ["유재석","조세호","박명수"]
# print(subway)

# #조세호씨가 몇번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)

# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호",20,True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전

# cabinet ={3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) key 5의 값이 없어서 오류 발생
# print(cabinet.get(5)) 
# print(cabinet.get(5,"사용가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet ={"A-3":"유재석","B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["c-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") 튜플은 add를 지원안함

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

# (name,age,hobby) = ("김종국",20,"코딩")
# print(name,age,hobby)

# # 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (jave 와 python 을 모두 할수있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python 을 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java 를 잊었어요
# java.remove("김태호")
# print(java)

# # 자료구조의 변경
# menu ={"커피", "우유", "주스"}
# print(menu,type(menu))

# menu = list(menu)
# print(menu,type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# menu = set(menu)
# print(menu,type(menu))

# #if
# weather = "비"
# weather = "미세먼지"
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세여")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("다필요없어")

# temp = int(input("기온은 어때요? "))
# if 30<= temp:
#     print("너무더워요")
# elif 10 <= temp and temp <30:
#     print("좋은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워")

# #for
# for waiting_no in [0,1,2,3,4,5]:
# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:     
#     print("{0}, 커피가 준비 되었습니다.".format(customer))

# # #while
# customer ="토르"
# index = 5
# while index >=1:
#     print("{0},커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0},커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
#     index += 1

# customer = "토르"
# person = "UnKnown"
# while person != customer :
#     print("{0},커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


# #continue 와 break
# absent = [2,5] # 결석
# no_book = [7] # 책없음
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# #한 줄 for
#  출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104.
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in stud ent]
# print(student)

# # 학생 이름을 길이로 변환
# student = ["Iron man","Thor","I am groot"]
# student = [len(i) for i in student]
# print(student)

# # 학생 이름을 대문자로 변환 
# student = ["Iron man","Thor","I am groot"]
# student = [i.upper() for i in student]
# print(student)

## 함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다")

# open_account()

## 전달값과 반환값
# def deposit(balance,money):
#     print("입급이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance,money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("잔액이 부족합니다. 현재 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance,money):
#     commision = 100 # 수수료 100원
#     return commision, balance - money - commision

# balance = 0 # 잔액
# balance = deposit(balance,1000) # 입금
# balance = withdraw(balance,2000) # 출금
# balance = withdraw(balance,500) 
# commision,balance = withdraw_night(balance,500) # 수수료 포함해서 출금
# print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commision,balance))

##기본값

# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {0} \t 나이 : {1} \t 주 사용하는 언어 : {2}".format(name,age,main_lang))
    
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")
# profile("유재석")
# profile("김태호")


## 키워드 값
# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(name ="유재석", main_lang = 20, age ="파이썬")
# profile(main_lang ="유재석", age = 25, name ="파이썬")

##가변인자

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0} \t나이 : {1} \t  ".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# def profile(name,age,*language):
#     print("이름 : {0} \t나이 : {1} \t  ".format(name,age),end=" ")
#     for lang in language:
#         print(lang,end =" ")
#     print("")

# profile("유재석",20,"Python","Java","C","C++","C#")
# profile("김태호",25,"Kotlin","Swift","","","")

## 지역 변수와 전역 

gun= 10

# 오류 발생  #함수내에 gun이 지정되어 있지 않다
# def checkpoint(soldiers):
#     gun = gun - soldiers  
#     print("[함수 내 ] 남은 총 : {0}".format(gun))

# 오류 해결 글로벌 함수로 외부에서 gun을 가져옴
# def checkpoint(soldiers):
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun  - soldiers  # 함수 내에서 gun라는 값이 지정되어 있지 않다
#     print("[함수 내 ] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun,soldiers):
#     gun = gun -soldiers
#     print("[함수 내 ] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun,2)
# print("전체 총 : {0}".format(gun))

##표준입출력

##sep을 붙임으로써 사이사이에 해당하는 것 집어넣어준다.
## end를 붙임으로써 print 문이 한줄에 나타난다.
# print("Python","Java",sep=",",end ="?")
# print("무엇이 더 재밌을까요?")

##표준에러 ?
# import sys
# print("Python","Java",file=sys.stdout)
# print("Python","Java",file=sys.stderr)

# #시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":")# ljust, rjust  통해 왼쪽과 오른쪽 값의 공간을 배정가능

# # 은생 대기순번표
# # 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3))# 3개의 공간에 값을 채우고 값이 없는공간에 0을 채워준다

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 "+ answer + "입니다.")

##다양한 출력 포맷

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000))
# print("{0:+,}".format(-100000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈자리는 ^ 로 채워주기 
# print("{0:^<+30,}".format(100000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# #파일 입출력

# #파일 생성 및 내용 입력
# score_file = open("D:\Github\-Babo\mission\score.txt","w",encoding="utf8")
# print("수학 : 0",file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()

## 파일 내용 추가 입력
# score_file = open("D:\Github\-Babo\mission\score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 내용 읽기
score_file = open("D:\Github\-Babo\mission\score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

