saying = "Don`t panic!"
letters = list(saying)

print(letters)
print(letters[0:10:3])
print(letters[3:10:2])

book = "The Hitchhiker`s Guide to the Galaxy"
booklist = list(book)
print(booklist)
book = ''.join(booklist[13:3:-1])
print(book)



# 리스트는 시작, 중지, 스텝을 이해합니다.
# 리스트에서 시작값은 시작할 인덱스 값을 의미합니다.
# 중간값은 range가 언제 끝날지 제어합니다.
# 스텝값은 range 생성 방법을 제어합니다.
# booklist [시작:중지:스텝]