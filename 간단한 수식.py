print(2 + 3 * 4) #2더하기3곱하기4( 2 + 3 * 4)를 계산하여 14를 출력한다.
print((2 + 3) * 4)#괄호안 2더하기3을 먼저 계산후 4를 곱하여((2+3)*4) 계산하고 20을 출력한다.
number = 2 + 3 * 4 #2+3*4를 number라는 변수에 값을 지정한다.
print(number) # 14 반환

# number = number +2와 number += 2는 같은 의미이다.
number = number + 2 
#   2+3*4를 지정한  number라는 변수에 
#   2를 더하여 새로운 number에 지정한다. 
print ( number ) #16 반환
number += 2
#   2+3*4+2를 지정한 
#   number라는 변수에 
#   2를 더하여 새로운 number에 지정한다. 
print(number ) #18 반환
number *= 2 
#   2+3*4+2+2를 지정한 
#   number라는 변수에 
#   2를 곱하여 새로운 number에 지정한다. 
print(number) #36 반환
number /= 2
#   2+3*4+2+2*2를 지정한 
#   number라는 변수에 
#   2를 나누어 새로운 number에 지정한다. 
print(number) # 18 반환
number -= 2
#   2+3*4+2+2*2/2를 지정한 
#   number라는 변수에 
#   2를 빼서 새로운 number에 지정한다.
print(number) # 18 반환
number %= 5
#   2+3*4+2+2*2/2-2를 지정한 
#   number라는 변수에 
#   2를 나누어 나머지 값을 새로운 number에 지정한다.
print(number) # 1 반환

# (abs)는 절댓값, (pow)는 제곱 값, 
# (max)는 괄호안에 가장큰수,
# (min)은 괄호안 가장 작은수,
# (round)는 반올림
print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))  
print(round(3.14))
print(round(4.99))

#(floor)은 소수점을 내림,
#(ceil)은 소수점을 올림,
#(sqrt)는 제곱근
from math import * 
# from math import는 math 라이브러리안에 모든것을 이용하겠다란 뜻
print(floor(4.99)) # 4
print(ceil(3.14)) # 4
print(sqrt(16)) # 4  
print(sqrt(9)) # 3

#파이썬에서 제공하는 random라이브러리를 사용하는것
from random import *

print(random())
 # random 함수에서 0.0~1.0 미만의 임의의 값 생성
print(random() * 10)
 #random 함수에서 0.0~10.0 미만의 임의의 값 생성
print(int(random() * 10 ))
 #(random() * 10 ) random함수에서
 #  0~ 10 미만의 임의의 정수값 생성
print(int(random() * 10 ) + 1) 
#(random() * 10 ) + 1) 안에 random함수에서
#  1 ~ 10 미만의 임의의 정수값을 생성
print(int(random() * 45) + 1 )
print(int(random() * 45) + 1 )
print(int(random() * 45) + 1 )
print(int(random() * 45) + 1 )
print(int(random() * 45) + 1 )
print(int(random() * 45) + 1 )

#(randrange)는 1~46이하의 숫자를 뽑아줌
print(randrange(1,46)) # 1~46미만의 임의의 값
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))

print(randint(1,45)) 
#(randint)는 1~45면 양끝 자리수 모두 뽑는 단어



#               Quiz!
# 당신은 최근에 코딩 스터디 모임을 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로,
# 1 번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 
# 프로그램을 작성하시오.

#                   조건
# 1.랜덤으로 날짜를 뽑아야함.
# 2.월별 날짜는 다름을 감안하여
#           최소 일수인 28일 이내로 정함
# 3.매월 1~3일은 스터디 준비를 해야하므로 제외


#          출력문 예제
# 오프라인 스터디 모임 날짜는 
# 매월 x 일로 선정되었습니다.

from random import* 
day = randint( 4,28 )
print("오프라인 스터디 모임 날짜는 매월"+ str(day) + "일로 선정되었습니다.")