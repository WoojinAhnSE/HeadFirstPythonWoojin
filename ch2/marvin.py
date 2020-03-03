paranoid_android = 'Marvin, the Paranoid Android'
letters = list(paranoid_android)
for char in letters[:6]:
  print('\t', char)
print()
for char in letters[-7:]:
  print('\t'*2, char)
print()
for char in letters[12:-8]:
  print('\t'*3, char)




# \t 로 인해 앞에 탭 문자가 추가됨