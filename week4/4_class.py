# # 1.if 조건문

# 연필가격 = 2000
# 펜가격 = 3000
# 연필개수 = int(input("연필 개수를 입력: "))
# 펜개수 = int(input("펜 개수를 입력: "))
# 총액 = 연필가격 * 연필개수 + 펜가격 * 펜개수

# if 총액 > 20000 :
#     총액 = 총액 * 0.9
#     print(f"10% 할인한 결제 금액: {int(총액)}원")
# else :
#     print(f"결제 금액: {int(총액)}원")

###########################

# # 2. if ~ else 조건문

# 나이 = int(input("나이를 입력: "))

# if 나이 >= 20 :
#     print("성인!")
# else :
#     print("미성년자!")

###########################

# # 3. if ~ else 조건문 2

# num = int(input("주민번호 8번째 숫자 입력: "))

# if num % 2 == 1 :
#     print("남자!")

# else :
#     print("여자!")

###########################

# # 4. if 중첩

# age = int(input("나이를 입력: "))
# height = float(input("키를 입력: "))

# if age > 12 :
#     if height > 150 :
#         print("놀이기구 이용가능")
#     else :
#         print("키 때문에 놀이기구 이용 불가능")
# else :
#     print("나이 때문에 놀이기구 이용 불가능")

###########################

# # 4_1. if 중첩 2

# age = int(input("나이를 입력: "))
# height = int(input("키를 입력: "))

# if age > 12 and height > 150 :
#     print("놀이기구 이용가능")
# else :
#     print("놀이기구 이용불가능")

###########################

# # 5. if 중첩

# 필기점수 = int(input("필기 점수 입력: "))
# 코딩결과 = input("코딩 시험 결과 입력: (합격 / 불합격): ")

# if 필기점수 >= 90 and 코딩결과 == "합격" :
#     print("최종합격")
# else :
#     print("최종불합격")

