for j in range(1, 10):
    for i in range(2, 10):
        print('{}X{}={}'.format(j, i, j*i)) # i 에 2에서 10까지의 변수를 루프할대마다 보냄
                                            # j 는 i 가 2에서 10까지 변수한 루프를 다하면
                                            # j의 루프가 2로 넘어감 9까지 반복

students = [90, 25, 67, 45, 80]

number = 0

for i in students:
    number = number + 1 
    if i >= 60:
        print('%d번 학생은 합격입니다.' %number)
    else:
        print('%d번 학생은 불합격입니다.' %number)   