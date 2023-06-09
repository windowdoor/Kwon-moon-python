#print(" a " + " b ")

# 방법 1
print("나는 % d살 입니다." % 24 ) # %d 는 정수값만 가능
print("나는 %s를 좋아해요" % "파이썬") # %s 는 원하는 문구열을 가져와 사용가능
print(" Apple은 %c로 시작해요." % "A") # %c 는 문자 하나만 가능
# %s는 문자열이든 문자든 정수든 다가져와 사용가능.
print("나는 % d살 입니다." % 24 )
print("나는 %s 색과 %s을 좋아해요 " % ("파랑", "빨강")) 
            # (나는 %s 색과 %s을 좋아해요 " % ("파랑", "빨강"))에서 "나는 %s 색과 %s을 좋아해요"에서 %S를 %("파랑, 빨강")으로 대입시켜 
            #나는 파랑색과 빨강을 좋아해요로 반환.

# 방법 2
print("나는 {}살 입니다.".format(24)) 
            # ("나는 {}살 입니다.".format(24))은 "나는 {}살입니다."에서
            # '.format()' 을 통해 .format뒤에 있는 괄호안 숫자(24)를 {}에 대입시켜 반환해준다.

print("나는 {}색과 {}을 좋아해요 " .format("파랑", "빨강"))
            #("나는 {}색과 {}을 좋아해요 " .format("파랑", "빨강"))은 "나는 {}색과 {}을 좋아해요"에서
            # '.format()' 을 통해 '.format()'뒤에 있는 괄호안 문자("파랑", "빨강")을 {} (중괄호)에 대입시켜 반환해준다.

print("나는 {0}색과 {1}을 좋아해요 " .format("파랑", "빨강"))
           #("나는 {}색과 {}을 좋아해요 " .format("파랑", "빨강"))은 "나는 {}색과 {}을 좋아해요"에서
           # '.format()' 을 통해 '.format()'뒤에 있는 괄호안 문자("파랑", "빨강")에서 "파랑"이 0번째가 되고 "빨강"이 1번째가 되어
           #  {} (중괄호)안에 숫자를 대입시켜 반환해주어 
           # "나는 파랑색과 빨강을 좋아해요"가 출려된다.

print("나는 {1}색과 {0}을 좋아해요 " .format("파랑", "빨강"))
            # ("나는 {}색과 {}을 좋아해요 " .format("파랑", "빨강"))은 "나는 {}색과 {}을 좋아해요"에서
            # '.format()' 을 통해 '.format()'뒤에 있는 괄호안 문자("파랑", "빨강")에서 "파랑"이 0번째가 되고 "빨강"이 1번째가 되어
            #  {} (중괄호)안에 숫자를 넣어 대입시켜 반환해주어
            #  "나는 빨강색과 파랑을 좋아해요"가 출력된다.

# 방법 3
print("나는 {age} 살이며, {color}색을 좋아해요".format(age=24, color = "빨간"))
            # ("나는 {age} 살이며, {color}색을 좋아해요".format(age=24, color = "빨간"))은 "나는 {age} 살이며, {color}색을 좋아해요"에서
            # '.format()' 을 통해 '.format()'뒤에 있는 괄호안 문자(age = 24, color = "빨간" )에서 age란 변수에 '24' 를 대입하게되고
            #  color란 변수에 "빨간"을 대입시켜 {} (중괄호)안에 문자를 넣어 대입시켜 반환해주어
            #  "나는 24살이며, 빨간색을 좋아해요"를 출력하게된다.
print("나는 {age} 살이며, {color}색을 좋아해요".format (color = "빨간", age=24, ))
            # ("나는 {age} 살이며, {color}색을 좋아해요".format(age=24, color = "빨간"))은 "나는 {age} 살이며, {color}색을 좋아해요"에서
            # '.format()' 을 통해 '.format()'뒤에 있는 괄호안 문자(age = 24, color = "빨간" )에서 age란 변수에 '24' 를 대입하게되고
            #  color란 변수에 "빨간"을 대입시켜 {} (중괄호)안에 문자를 넣어 대입시켜 반환해주어
            #  "나는 24살이며, 빨간색을 좋아해요"를 출력하게된다.

# 방법 4
age = 24
color = " 파랑 "
print(f"나는 { age }살이며, {color}색을 좋아해요.")
            # age와 color라는 변수를 만들어 age에는 '24'를, color에는 '파랑'을 대입시켜 
            # print(f"나는 { age }살이며, {color}색을 좋아해요.")에서 괄호안 첫자에 있는(f)를 활용해 {}(중괄호) 안에 변수를 넣어
            # (f"나는 { age }살이며, {color}색을 좋아해요.")를 출력하여 "나는 24살이며 파랑색을 좋아해요"가 출력된다.

    