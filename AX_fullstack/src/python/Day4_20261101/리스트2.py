#장바구니에 물건을 추가하듯, 게시판 게시글을 추가 하듯
#유튜브 댓글 댓글을 추가하듯
#여러개의 데이터를 저장하는 타입(List)

#비어있는 바구니! 하나가 생긴다
장바구니 = []
print(장바구니)
#len은 사이즈 구하는 기능
장바구니개수 = len(장바구니)
print("현재 개수", 장바구니개수)

# 담기 버튼을 클릭했다는 가정하에 데이터를 추가하는 기능
장바구니.append("미역국")
장바구니.append("가글")

print(장바구니)
장바구니개수 = len(장바구니)
print("현재 개수", 장바구니개수)

장바구니.append("팝콘")
장바구니.append("샴푸")

print(장바구니)
장바구니개수 = len(장바구니)
print("현재 개수", 장바구니개수)

#추가되는 데이터는 항상 뒤쪽에 들어간다
#코드는 항상 위에서 아래로 실행된다

#삭제
# print("삭제 전에는 무조건 확인:", 장바구니)

#가글 삭제
# remove(값)

# select = input()
# try:
#     "가글" in 장바구니
#     장바구니.remove("가글")
#     print(장바구니)
# except:
#     print("없는 목록")

# 출근명단에서 이서희 사원이 출근 안했니?

# 출근명단 = ["에리나","알렉스","덱스","데빈"]

# if "이서희" not in 출근명단:
#     print("지각이다!!!!!")
# else:
#     print("정상 출근했다!")

# 아이디 중복확인
아이디목록 = ["qwer", "asdf", "zxcv"]
# print("사용 가능한 아이디입니다") if input().strip() not in 아이디목록 else print("중복입니다!\n다른 아이디를 입력하세요")
    
try:
    result = ""
    for c in input():
        if ('0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z'): result += c
    if not result and result not in 아이디목록:
        print("사용 가능한 아이디입니다") 
        아이디목록.append(result)
    else: print("중복입니다!\n다른 아이디를 입력하세요")
except: print("잘못된 문자열 입력")
