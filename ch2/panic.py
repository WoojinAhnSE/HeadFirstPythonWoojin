phrase = "Don`t panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
  plist.pop()
plist.remove('D')
plist.remove('`')
plist.extend([plist.pop(), plist.pop()])
plist.insert(2 ,plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
print(i)

# 리스트 메서드는 리스트의 원래 상태를 바꾸므로 파괴(destructive)동작 입니다.