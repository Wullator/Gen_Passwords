import random
g = int(input('Введи число символов в пароле: '))
str1 = '123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str1+str2+str2.upper()
ls = list(str3)
random.shuffle(ls)
psw = ''.join([random.choice(ls) for x in range(g)])
print(psw)
