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
