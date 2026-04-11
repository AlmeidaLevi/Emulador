def to_signed(value, bits): #Garante que o valor mantenha o sinal
    if value & (1 << (bits - 1)):
        return value - (1 << bits)
    return value

def two_complement(num, bits):
    mask = (1 << bits) - 1
    return (num ^ mask) + 1

def is_bigger_than(num1, num2, bits):
    difference = num1 + two_complement(num2, bits)
    signed = (difference >> (bits - 1)) & 1

    if not signed:
        return True
    return False

def booth_multiply(A, Q, M, Q_1, n, bits):
    mask = (1 << bits) - 1

    if not (Q & 0b1) and Q_1:
        A = to_signed((A + M) & mask, bits)

    elif (Q & 0b1) and not Q_1:
        A = to_signed((A - M) & mask, bits)

    lsb_A = A & 0b1 #LSB de A
    lsb_Q = Q & 0b1 #LSB de B

    Q_1 = lsb_Q

    Q = ((Q >> 1) | (lsb_A << (bits - 1))) & mask #Q é deslocado 1 bit para a direita e seu MSB recebe o LSB de A

    if A & (1 << (bits - 1)):
        A = (A >> 1) | (1 << (bits - 1)) #Se A era negativo, permanece negativo
    else:
        A = A >> 1

    A = to_signed(A & mask, bits)

    n -= 1 #Decresce o número de passos restantes

    if n > 0:
        return booth_multiply(A, Q, M, Q_1, n, bits)

    result = ((A & mask) << bits) | Q # Retorna o resultado (A é a metade mais significativa e Q, a menos)

    return to_signed(result, bits * 2)


def division(num1, num2, bits):
    mask = (1 << bits) - 1

    msb_num1 = (num1 >> (bits - 1)) & 1
    msb_num2 = (num2 >> (bits - 1)) & 1

    signed = msb_num1 ^ msb_num2

    if msb_num1:
        num1 = two_complement(num1, bits) & mask

    if msb_num2:
        num2 = two_complement(num2, bits) & mask

    A = 0
    n = 1
    while n <= bits:
        msb_num1 = (num1 >> (bits - 1)) & 1

        A = (A << 1) & mask
        A = A | msb_num1
        num1 = (num1 << 1) & mask

        if is_bigger_than(A, num2, bits):
            A = (A - num2) & mask
            num1 = num1 | 0b1
        else:
            num1 = num1 | 0b0

        n += 1

    if signed:
        num1 = two_complement(num1, bits) & mask
        A = two_complement(A, bits) & mask

    return to_signed(num1, bits), to_signed(A, bits)
