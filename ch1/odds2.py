from datetime import datetime
import time
import random

odds = [ 1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30, 31, 33, 35,
 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute

for i in range(5):
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute")
    time.sleep(random.randint(1,10))

print(i)


# 여기에서 i 가 4가 나오는 이유가 무엇 일까요? 답 = i 구문을 반복하는 횟수를 정의 --> 0, 1, 2, 3, 4
# 리스트는 여러 개의 원소를 포함하는 하나의 집합체 대괄호 [] 로 표현
# 특정한 원소들의 순서들을 인덱스 라고 표현
# 튜플은 다양한 데이터를 담을 수 있고 내용을 변경할 수 있는 시퀸스 다. 소괄호 () 로 표현
# 시퀀스(sequence)는 데이터에 순서(번호)를 붙여 나열한 것이다.
# 파이썬 시퀀스의 종류는 리스트(list), 튜플(tuple), 레인지(range), 문자열(string) 등 여러가지를 제공

