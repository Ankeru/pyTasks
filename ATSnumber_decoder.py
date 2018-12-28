#Task (Russian): 
# Написать программу декодирования телефонного номера для АОН. 
# По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
# — Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
# — Каждая значащая цифра повторяется минимум 2 раза
# — Если в номере идут несколько цифр подряд, то для обозначения «такая же цифра как предыдущая» используется идущий 2 или более подряд раз знак #
# Проверка: входящая строка 4434###552222311333661 соответствует номеру 4452136
# Регулярные выражения использовать в этих заданиях — нельзя :)
#python version 3.7.0
inputNumber = '4434###552222311333661'
decodedNumber = ''
for i in range(1, len(inputNumber)):
    if inputNumber[i] == '#':
        if inputNumber[i-1] == '#':
            if (decodedNumber != ''):
                if len(decodedNumber) >= 2:
                    if  (decodedNumber[-1] != decodedNumber[-2]):
                        decodedNumber += decodedNumber[-1]
                else: 
                    decodedNumber += decodedNumber[-1]
    elif inputNumber[i] == inputNumber[i-1]:
        if (decodedNumber != ''):
            if inputNumber[i] != decodedNumber[-1]:
                decodedNumber += inputNumber[i]
        else: 
            decodedNumber += inputNumber[i]
print('Decoded number is: ' + str(decodedNumber))
