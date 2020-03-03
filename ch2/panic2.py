phrase = "Don`t panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[-5], plist[-6]])


print(plist)
print(new_phrase)


# 리스트에서 특정 객체만 추출하고 기존 리스트는 바꾸지 않기 때문에 비파괴(nondistructive) 동작입니다.
# 조인(join) 메서드에 ''이 붙는 이유?