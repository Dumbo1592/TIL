import random

# def up_down():
#     n = random.randint(1, 100)
#     while 1:
#         user = int(input("1~100의 숫자 중 하나 입력하시요:"))
#         if user < n:
#             print("up")
#         elif user > n:
#             print("down")
#         else:
#             print("정답")
#             break

# UpnDown()
    
# def open_safe(user):
#     password = "2468"
#     print("열림") if password == user else print("다르면 비밀번호를 확인하시오")

# Open_safe(input())

# def rock_paper_scissors(user):
#     if user != "가위" and user != "바위" and user != "보":
#         print("잘못된 선택")
#     else: print(random.choice(["승리","패배","무승부"]))

# Rock_Paper_Scissors(input())

# def grade_cal(score):
#     if 90 >= score:
#         print('A')
#     elif 80 >= score:
#         print('A')
#     elif 70 >=score:
#         print('B')
#     else:
#         print('C')

# grade_cal(int(input()))

# def cal(bill):
#     dis = 0
#     if bill >= 30000:
#         bill -= 3000
#         dis = 3000
#     elif bill >= 20000:
#         bill -= 2000
#         dis = 2000
#     elif bill >= 10000:
#         bill -= 1000
#         dis = 1000
    
#     print(f"할인 금액:{dis}, 최종 결제 금액:{bill}")

# cal(35000)

# def kiosk(sel):
#     menu = [
#         ["아메리카노", 3000],
#         ["카페라떼", 4000],
#         ["딸기스무디", 5000]
#     ]
#     if sel > len(menu): print("없는 메뉴")
#     else: print(f"메뉴 {sel}번은 {menu[sel-1][0]} {menu[sel-1][1]}원입니다")

# kiosk(int(input()))

# def taxi_charge(km):
#     if km > 10:
#         print("18000원입니다")
#     elif km > 5:
#         print("12000원입니다")
#     elif km > 2:
#         print("8000원입니다")
#     else:  
#         print("5000원입니다")

# taxi_charge(int(input()))

