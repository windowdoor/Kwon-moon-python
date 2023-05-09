python = "Python is Amazing"# python이란 변수에 Python is Amazing이란 문장을 대입
print(python.lower())# (python.lower())은 python 이란 변수에(.lower())을 넣어 글자를 소문자로 바꿔줄때 쓰인다.
print(python.upper())# (python.upper())은 python 이란 변수에(.upper())을 넣어 글자를 대문자로 바꿔줄때 쓰인다.

print(python[0].isupper()) # 답 : true
        # (python[0].isupper())은 python 이란 변수에(.isupper())을 넣어 첫번째 글자가 대문자인지 알아볼때 쓰인다.
print(python[0].islower()) # 답 : false
        # (python[0].islower())은 python 이란 변수에(.islower())을 넣어 첫번째 글자가 소문자인지 알아볼때 쓰인다.

print(len(python)) # (len(python))은 python이란 변수의 글자 갯수가 몇개인지 세어낼때 쓰인다.
print(python.replace("Python"," C++")) 
        # (python.replace("Python"," C++")은 python이란 변수안에 replace("Python"," C++") 를 사용해
        # python이란 변수안 "Python is Amazing"에서 "C++ "로 바꾸어 "C++ is Amazing"으로 반환해줄때 쓰인다.

index = python. index("n") #index("n")은 python이란 변수안에서 "n"이라는 글자가 몇뻔째로 위치해 있는지 알아볼때 쓰인다.
print(index)
index = python. index("n", index + 1)
        # index("n" + 1)은 python이란 변수안에서 "n"이라는 글자가
        # 첫번째로 나온 이후에 다음"n"이라는
        # 글자가 아디에 위치해 있는지 알아볼때 쓰인다.
print(index)

print(python.find("A")) # 
print(python.find("C++"))
#print(python. index("C++"))

(python.count("n")) # (python.count("n"))이란 python이란 변수에 count("n")을 이용하여 n 이란 단어가 몇개 있는지 세어줄때 쓰인다.
