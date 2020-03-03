from datetime import datetime

today = datetime.today().weekday()

if today == 5:
    print('Party!')
elif today == 6:
    print('Recover .')
else:
    print('work, work, work.')
