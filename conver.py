import sys


def dec_bi(dec):
    dec = int(dec)
    res = []
    while dec > 1:
        res.append(dec%2)
        dec /= 2
    soma = -1
    while abs(soma) <= len(res):
        print(res[soma], end=' ')
        soma -= 1

def dec_hex(dec):
    dec = int(dec)
    cc = []
    r = []

    if dec <= 15:
        cc.append(dec)
    elif dec > 15:   
        while dec > 15:
            cc.append(dec%16)
            dec /= 16
        if dec < 16:
            cc.append(dec)       
    else:
        print('Entrada invalida. ')
        sys.exit()

    for n in cc:
        if n >= 1 and n < 10:
            r.append(n)
        elif n >= 10 and n < 11:
            n = 'a'
            r.append(n)
        elif n >= 11 and n < 12:
            n = 'b'
            r.append(n)
        elif n >= 12 and n < 13:
            n = 'c'
            r.append(n)
        elif n >= 13 and n < 14:
            n = 'd'
            r.append(n)
        elif n >= 14 and n < 15:
            n = 'e'
            r.append(n)
        elif n >= 15 and n < 16:
            n = 'f'
            r.append(n)
        else:
            print('erro de digitação. ')
            break
    
    soma = -1
    for n in r:
        print(r[soma], end='  ')
        soma -= 1

def dec_oct(dec):
    dec = int(dec)
    rest = []
    r = []

    if dec < 8:
        rest.append(dec)
    elif dec >= 8:
        while dec >= 8:
            rest.append(dec%8)
            dec /= 8
        if dec < 8:
            rest.append(dec)
    else:
        print('Entrada errada. ')
        sys.exit()

    for n in rest:
        if n >= 1 and n < 8:
            r.append(n)
        elif n >= 8 and n < 9:
            n = '10'
            r.append(n)
        elif n >= 9 and n < 10:
            n = '11'
            r.append(n)
        elif n >= 10 and n < 11:
            n = '12'
            r.append(n)
        elif n >= 11 and n < 12:
            n = '13'
            r.append(n)
        elif n >= 12 and n < 13:
            n = '14'
            r.append(n)
        elif n >= 13 and n < 14:
            n = '15'
            r.append(n)
        elif n >= 14 and n < 15:
            n = '16'
            r.append(n)
        elif n >= 15 and n < 16:
            n = '17'
            r.append(n)
        else:
            break

    soma = -1
    for n in rest:
        print(rest[soma], end=' ')
        soma -= 1
        
def bi_dec(bi):
    rep = len(bi)
    m = 1
    m = 2**(rep-1)
    r = 0
    for n in bi:
        if n == '1':
            r += m
        elif n == '0':
            r += 0
        else:
            print('erro de digitação. ')
            sys.exit()
        m /= 2
    return(r)
    
def hex_dec(hex):
    cc = []
    hexd = []
    soma = 0
    for n in range (len(hex)):
        hexd.append(hex[soma])
        soma += 1

    for n in hexd:
        if n == '0' or n == '1' or n == '2' or n == '3' or n == '4' or n == '5' or n == '6' or n == '7' or n == '8' or n == '9':
            cc.append(int(n))
        elif n == 'a':
            cc.append(10)
        elif n == 'b':
            cc.append(11) 
        elif n == 'c':
            cc.append(12)
        elif n == 'd':
            cc.append(13)
        elif n == 'e':
            cc.append(14)
        elif n == 'f':
            cc.append(15)
        else:
            print('Digitação errada. ')
            sys.exit()
            
    r = 0      
    exp = 0
    pos = -1
    for n in range(len(hex)):
        r += (16**exp)*cc[pos]
        pos -= 1
        exp += 1
    return(r)

def oct_dec(oct):
    octd = []
    soma = 0
    for n in range (len(oct)):
        octd.append(int(oct[soma]))
        soma += 1

    for n in octd:
        if n > 7:
            print('Base octal não aceita digitos maiores que 7. ')
            sys.exit()

    dec = 0      
    exp = 0
    pos = -1
    for n in range(len(oct)):
        dec += (8**exp)*octd[pos]
        pos -= 1
        exp += 1
    
    return(dec)

op1 = input('Base numero que o numero esta: ')
op2 = input('Base em que vc quer converter: ')
numinput = input('Numero a ser convertido: ')

if op1 == 'decimal':
    if op2 == 'binario':
        dec_bi(numinput)
    elif op2 == 'hexadecimal':
        dec_hex(numinput)
    elif op2 == 'octal':
        dec_oct(numinput)
    else:
        print('Erro de digitação. ')

elif op1 == 'binario':
    if op2 == 'decimal':
        print(bi_dec(numinput))
    elif op2 == 'octal':
        dec_oct(bi_dec(numinput))
    elif op2 == 'hexadecimal':
        dec_hex(bi_dec(numinput))
    else:
        print('Erro de digitação. ')

elif op1 == 'hexadecimal':
    if op2 == 'decimal':
        hex_dec(numinput)
    elif op2 == 'binario':
        dec_bi(hex_dec(numinput))
    elif op2 == 'octal':
        dec_oct(hex_dec(numinput))
    else:
        print('Erro de digitação. ')

elif op1 == 'octal':
    if op2 == 'decimal':
        print(oct_dec(numinput))
    elif op2 == 'binario':
        dec_bi(oct_dec(numinput))
    elif op2 == 'hexadecimal':
        dec_hex(oct_dec(numinput))
    else:
        print('Erro de digitação. ')

else:
    print('Erro de digitação. ')

    
    










        