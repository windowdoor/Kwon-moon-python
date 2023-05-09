print( "백문이 불여일견\n 백견이 불여일타") 
# \n 은 줄바꿈으로서 
# 백문이 불여 일견 백견이 불여일타를 
#백문이 불여일견
#백견이 불여일타로 출력할수있게 줄을 바꾸어줌
print('저는 "나도코딩" 입니다.')
#'저는 "나도코딩" 입니다.'에서 
# ''의 문장 안에서 ""를 인식해 
#저는 "나도코딩" 입니다.로 출력 해줌

print("저는 \"권문\" 입니다")
#"저는 "권문" 입니다"에서 
# "저는 \"권문\" 입니다" 로 역슬레시(\)를 사용해
# ""를 문장안에서 출력할수있게 해줌
#           \'\"는 문자내에서 따옴표이다.

print("저는 \'권문\'입니다.")
#("저는 \'권문\'입니다.")에서
# "저는 \'권문\' 입니다" 로 역슬레시(\)를 사용해
# '를 문장안에서 출력할수있게 해줌
#           \'\"는 문자내에서 따옴표이다.

print(" C:\\Users\\woong\\OneDrive")
#(" C:\\Users\\woong\\OneDrive")는 
# 원래(" C:\Users\woong\OneDrive")로 써야 맞지만 
#문장내에서 역슬레시(\)를 하나만 쓰면 출력이 오류가
# 떠서 문장 내에서 역슬레시를 표현하기 위해서는 
# 역슬레시를 한번이 아닌 (\) =  X
# 역 슬레시를 두번 기입 (\\) 한다. = O

print("Red Apple\rpine")
#("Red Apple\rpine")에서 \r은 커서를 맨앞으로 이동하기
# 위해 쓰이는 문자이다. 따라서 ("Red Apple\rpine")속에
#Apple\r뒤에 pine 이란 단어가 Apple앞 
# "Red(띄어쓰기)" 까지 포함해 pineApple을 출력한다.

print("Redd\b Apple")
# print("Redd\b Apple") 에서 
# ("Redd")이 처럼 Red 뒤에 d 라는 오타가 있어 한글자
# 지우고 싶다면 \b를 사용해 한글자를 삭제하면
# Red Apple 을 출력하게 된다.
# 따라서 \b 는 백스페이스 (한글자 삭제)하고 생각하면된다.

print ("Red \t Apple")
#print ("Red \t Apple")에서
# 출력했을때 문장 내에서 탭 만큼 띄우고 싶다면 
# 위와 같이 "Red \ t Apple" 을 작성하면
#   \t 를사용하여 문장의 칸을 탭 만큼 띄운다
# 따라서 "Red   Apple"로 출려된다.




#                   퀴즈
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com  
#규칙1 : http:// 부분은 제외 => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => nave
#규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 갯수 + "!"로 구성
#                    (nav)        (5)               (1)         (!)        
# 예) 생성된 비밀번호 : nav51!

internet = "naver"
print ( "생성된 비밀번호 :" + internet [0:3])
print ( len(internet) )
print (internet.count("e"))
print ("!")

#                       오답노트
url = "http://naver.com "
my_str = url.replace("http://","")
# repalce를 이용하여 "http://naver.com "에서 
# "http://" => "" 바꿔주어 "http://"가 없어져 naver.com 만 남게 된다.

#print(my_str)
my_str = my_str[:my_str.index(".")]
# my_str 이란 변수에서 .index를 사용해 naver.com이란
# 문장안에 .직전까지만 놔두고[] 뒤에 있는 .com을 없애주어,
# naver만 남게 된다.    my_str[0:5] => 0 ~ 5 직전까지 )

#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# my_str[:3]로 인해 my_str이란 변수에 0~3번까지 글자를 반환하고
# (len(my_str))이처럼 len을 사용해 my_str이란 변수에 글자를 반환함.
#(my_str.count("e"))이처럼 my_str이란 변수에 
# count를 사용해("e") 라는 문자의 개수가 몇개인지 반환해준다.
#위에 len과 count를 문자열로 바꾸어주기위해 str을 앞에 붙여 사용한다.


print("{} 의 비밀번호는 {} 입니다.".format(url,password))
#