#애완동물을 소개 하세요.
animal = "강아지" #animal 이란 변수에 "강아지"로 설정
name = "원두" #name 이란 변수에 "원두"로 설정
age = 4 #age 란 변수에 4를 설정
hobby = "산책" #hobby란 변수에 "산책"으로 설정
is_adult = age >= 3 #is_adult란 변수에 age >=3을 설정
print("우리집 강아지는 원두에요") #print는 출력을 위한 명령문이고 "우리집 강아지는 원두에요" 를 출력한다.
print("원두는 4개월이며 산책을 아주 좋아해요")#print는 출력을 위한 명령문이고 "원두는 4개월이며 산책을 아주 좋아해요"를 출력한다.
print("원두는 어른일까요? True")#print는 출력을 위한 명령문이고 "ㅜ언두는 어른일까요? True"를 출력한다.

print("우리집" + animal + "이름은" + name + "에요") #print는 출력을 위한 명령문이고 설정한 단어에 맞게 "우리집 강아지는 원두에요"를 출력
print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요")#print는 출력을 위한 명령문이고 설정한 단어에 맞게 "원두는 4살이며 산책을 아주 좋아해요"를 출력
print(name + "는 어른일까요?" + str(is_adult))#print는 출력을 위한 명령문이고 설정한 단어를 포함해 "원두는 어른일까요?"를 True로 출력한다.


animal = "고양이"
name = "리호"
age = 4
hobby = "캣잎"
is_adult = age >=3
print("우리집"+ animal + "는" + name + "에요")#print는 출력을 위한 명령문이고 설정한 단어에 맞게 "우리집 고양이는 리호에요"를 출력
hobby = "공놀이"
print(name + "는" + str(age)+ "살이며" + hobby +"을 아주 좋아해요")#print는 출력을 위한 명령문이고 설정한 단어에 맞게 "리호는 4살이며 캣잎을 아주 좋아해요"를 출력      
print(name + "는 어른일까요?" +str(is_adult))#print는 출력을 위한 명령문이고 설정한 단어를 포함해 "리호는 어른일까요?"를 True로 출력한다.

#Quiz 변수를 이용하여 다음 문장을 출력하시오

# 변수명 = station
# 변수값 = "사당", "신도림", "인천공항" 순으로 입력

# 출력문장= xx 행 열차가 들어오고 있습니다.
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")#print는 출력을위한 명령문이고 설정한station에 맞춰 "사당행 열차가 들어오고 있습니다."를 출력
station = "신도림"
print(station + "행 열차가 들어오고 있습니다." )#print는 출력을위한 명령문이고 설정한station에 맞춰 "신도림행 열차가 들어오고 있습니다."를 출력
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")#print는 출력을위한 명령문이고 설정한station에 맞춰 "인천공항행 열차가 들어오고 있습니다."를 출력
station = "목동"
print(station + "행 열차가 들어오고 있습니다.")
