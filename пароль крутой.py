import random
adas=input('хотите пароль?')
while adas=='da':
    digits='1234567890'
    lowlet='asdfghjklqwertyuiop'
    biglet='ASDFGHJKLQWERTYUIOP'
    simv='/.,><?=+-_'
    parol=''
    dlin=int(input('КАКАЯ ДЛИННА'))
    civri=input('ВКЛЮЧАТЬ  ЦИФРЫ?')
    bukm=input('ВКЛЮЧАТЬ БОЛЬШИЕ БУКВЫ?')
    bukl=input('ВКЛЮЧАТЬ МЕЛКИЕ БУКВЫ.')
    simvol=input('ВКЛЮЧАТЬ СИМВОЛЫ?')
    while len(parol)<dlin:
        if bukm=='da':
            parol+=random.choice(biglet)
        if bukl=='da':
            parol+=random.choice(lowlet)
        if simvol=='da':
            parol+=random.choice(simv)
        if civri=='da':
            parol+=random.choice(digits)
    print(parol)
    adas=input('хотите еще раз?')
