jumin = "001002-3456789" #jumin 이란 변수에 주민번호를 등록.

print ( "성별 :" + jumin[7]) #jumin[7]은 jumin이란 변수에서 7번째 숫자를 빼기위해 쓰인다.
print (" 연도 :" + jumin[0:2])#jumin[0:2]는 jumin이란 변수에서 0부터 2번째 숫자직전까지를 빼기위해 쓰인다.
print (" 월 :" + jumin[2:4])#jumin[2:4]는 jumin이란 변수에서 2부터 4번째 숫자직전까지를 빼기위해 쓰인다.
print (" 일 :"+ jumin[4:6])#jumin[4:6]는 jumin이란 변수에서 4부터 6번째 숫자직전까지를 빼기위해 쓰인다. 

print ("생년 월일 :" + jumin[:6])# jumin[:6]은 jumin이란 변수에서 처음부터 6번째 숫자직전까지 빼기위해 쓰인다.
print (" 뒤 7자리 :" + jumin[7:14])# jumin[7:14]은 jumin이란 변수에서 7부터 14번째 숫자직전까지 빼기위해 쓰인다.
print (" 뒤 7자리 :" + jumin[7:])# jumin[7:]은 jumin이란 변수에서 7부터 끝까지 빼기위해 쓰인다.

print (" 뒤 7자리 (뒤에부터) :" + jumin[-7:])# jumin[-7:]은 jumin이란 변수 14자리를 뒤에서 7번째부터 끝까지 빼기위해 쓰인다.
print (" 앞 6자리 (뒤에부터) :" + jumin[-13:])# jumin[-14:]는 jumin이란 변수 14자리를 뒤에서 13번째부터 끝까지 빼기위해 쓰인다.