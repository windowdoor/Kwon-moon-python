#  리스트란 순서를가지는 개체의 집합!

#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20 ,30] #[]로 순서를 가진 집합체(리스트)를 만듦
print (subway)          # 따라서 [10,20,30]을 반환

subway = ["유재석", "조세호", "박명수"] #[]로 순서를 가진 집합체(리스트)를 만듦
print(subway)             # 따라서 ["유재석", "조세호", "박명수"]를 반환

# 질문 조세호가 몇 번째 칸에 타고있는가?
print(subway.index("조세호"))
#subway란 집합체에 index를 사용해 "조세호"란 값이 어디에 위치해있는지 반환


#질문 하하가 다음 정류장에 다음칸에 탐
subway.append("하하")
#subway란 집합체(리스트)에 append를 활용해 "하하"라는 값을 맨뒤에 추가
print(subway)               # 따라서 ["유재석", "조세호", "박명수", "하하"] 를 출력


#질문 정형돈을 유재석/조세호 사이에 추가
subway.insert(1,"정형돈")
#subway란 집합체(리스트)에 insert를 활용해 "정형돈"라는 값을 1번("조세호") 앞에 ("정형돈")을 추가
print(subway)                       # 따라서 ["유재석","정형돈","조세호","박명수", "하하"]를 출력


#지하철에 있는 사람들을 한명씩 빼냄
print(subway.pop())
#subway란 집합체(리스트)에 pop을 활용해 뒤에서부터 하나씩 뺄때 쓰인다.
print(subway)                       #따라서 ["유재석","정형돈","조세호","박명수"]를 출력

print(subway.pop())
#subway란 집합체(리스트)에 pop을 활용해 뒤에서부터 하나씩 뺄때 쓰인다.
print(subway)                       #따라서 ["유재석","정형돈","조세호"]를 출력

print(subway.pop())
#subway란 집합체(리스트)에 pop을 활용해 뒤에서부터 하나씩 뺄때 쓰인다.
print(subway)                       #따라서 ["유재석","정형돈"]을 출력

# 질문 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
#subway란 집합체(리스트)에 append를 활용해 뒤에 "유재석"을 추가한다.
print(subway)           #따라서 ['유재석', '정형돈', '유재석']을 출력
print(subway.count("유재석"))
#subway란 집합체(리스트)에 count를 활용해 
#subway란 집합체 안에 "유재석"이란 단어가 몇개 있는지 셀때쓰인다.
#따라서['유재석', '정형돈', '유재석']을 출력하기때문에 2를 출력한다.

#질문    정렬을 해보라
num_list = [5, 2, 3, 4, 1]
num_list.sort()
#num_list란 집합체(리스트)에 sort를 활용해
#num_list란 집합체 안에 순서가 어지럽혀있는
#  [5,2,3,4,1]의 숫자를 
#  [1,2,3,4,5]로 정렬해줄때쓰인다.
print(num_list)
#따라서 [1,2,3,4,5]가 출력 된다.


#질문   순서 뒤집기를 해보라
num_list.reverse()
#num_list란 집합체(리스트)에 reverse를 활용해
#num_list란 집합체 안에 순서가 어지럽혀있는
#  [5,2,3,4,1]의 숫자를 거꾸로 즉,[5,4,3,2,1]로 뒤집을때 쓰인다.
print(num_list)
#따라서 [5,4,3,2,1]이 출력 된다.


#질문  모두 지우기
num_list.clear()
#num_list란 집합체(리스트)에 clear를 활용해
#num_list란 집합테 안에있는 값을 모두 지울때 쓰인다.
print(subway)
#따라서 [] 값이 출력된다.

# 다양한 자료형 함께 사용
num_list = [5, 2, 3, 4, 1] 
mix_list = [20,"조세호", "true"]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
#num_list란 집합체(리스트)에 extend를 활용해(mix_list)를
#  num_list뒤에 붙여 사용할때 쓰인다.
print(num_list)
#따라서 [5,2,3,4,1,20,조세호,3]을 출력한다.

