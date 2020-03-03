word = "bottle"
for beer_num in range(99, 0, -1): # 99에서 0 까지 -1 씩 루프,'beer_num'를 루프반복 변수로 사용함
    print(beer_num, word, "of beer on the wall.") # 4개의 Print 함수로 현재 반복되는 노래가사를 출력함. 예를 들어
    print(beer_num, word, "of beer") # '99병의 맥주가 선반에 있네. 99병의 맥주. 한개를 집어서 건네주었네.' 등의 가사가 반복됨
    print("Take one down.") 
    print("Pass it around.")
    if beer_num == 1: # if 문으로 beer_num 변수가 1과 같으면 
        print("No more bottles of beer on the wall.") #다음 print문으로 종료
    else: # 그렇지 않다면
      new_num = beer_num -1 # new_num 를 beer_num 으로 할당
      if new_num ==1: # 만약에 new_num 변수가 1과 같으면
          word = "bottle" # "bottle" 이라는 문자열을 word 로 할당
          print(new_num, word, "of beer on the wall.") # 가사가 문법에 맞도록 'word' 변수의 값을 바꿔서 노래를 마무리함.
    print() # 반복문 끝에 공백을 출력해서 프로그램을 종료함 

