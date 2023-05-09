cabinet = {3:"유재석", 100:"김태호"}
#cabinet이란 변수에 3에는 유재석, 100에는 김태호를 설정
print(cabinet[3])
#cabinet이란 변수속 3을 "유재석"을 설정해 두었는데 
#print를 통해 cabonet이란 변수에서 3을 대괄호[]속에 집어 넣어 [3]을 통해서
#유재석이 출력 된다.
print(cabinet[100])
#cabinet이란 변수속 100을 "김태호"를 설정해 두었는데 
#print를 통해 cabonet이란 변수에서 100을 대괄호[]속에 집어 넣어 [100]을 통해서
#김태호가 출력 된다.

print(cabinet.get(3))
#cabinet이란 변수속 3을 "유재석"을 설정해 두었는데 
#cabinet이란 변수에서 3을 get()을 이용해
#소괄호()속에 집어 넣어 get(3)을 통해서
#유재석이 출력 된다.


#print(cabinet[5])


print(cabinet.get(5))
#cabinet이란 변수속 5라는 숫자를 설정해 놓지 않고 
#cabinet이란 변수속 get()을 이용해 출력을 해보려하니
#설정 값이 없기 때문에 NONE으로 출력된다.
#get() 은 오류는 나지 않고 NONE으로 출력된다.

print(cabinet.get(5,"사용가능"))
#cabinet이란 변수속 5라는 숫자를 설정해 놓지 않고 
#cabinet이란 변수속 get()을 이용해 출력을 해보려하니
#설정 값이 없기 때문에 NONE으로 출력된다.
#단, 만약 get(5)가 설정 값이 있다면 설정 값을 가져오겠지만.
#없다면 get(5, "사용가능")에서 "사용가능"을 출력 
print("hi")

print(3 in cabinet) #true
#cabinet이란 변수안에 in을 사용해 
#설정을 해놓은 것 이 있다면 true
#설정을 해놓은 것 이 없다면 false를 출력한다.
#따라서 3이 cabinet이란 변수에 설정했기 때문에 true를 출력한다.

print(5 in cabinet) #false
#cabinet이란 변수안에 in을 사용해 
#설정을 해놓은 것 이 있다면 true
#설정을 해놓은 것 이 없다면 false를 출력한다.
#따라서 5가 cabinet이란 변수에 설정을 해놓지 않았기 때문에 false를 출력한다.

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)


#손님 감
del cabinet["A-3"]
print(cabinet)

#key들 만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)