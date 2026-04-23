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

def booth_multiply(Q, M):
    mask = (1 << 32) - 1

    A = 0
    Q_1 = 0
    for i in range(0, 32):

        if not (Q & 0b1) and Q_1:
            A = to_signed((A + M) & mask, 32)

        elif (Q & 0b1) and not Q_1:
            A = to_signed((A - M) & mask, 32)

        lsb_A = A & 0b1 #LSB de A
        lsb_Q = Q & 0b1 #LSB de B

        Q_1 = lsb_Q

        Q = ((Q >> 1) | (lsb_A << (32 - 1))) & mask #Q é deslocado 1 bit para a direita e seu MSB recebe o LSB de A

        if A & (1 << (32 - 1)):
            A = (A >> 1) | (1 << (32 - 1)) #Se A era negativo, permanece negativo
        else:
            A = A >> 1

        A = to_signed(A & mask, 32)

    result = ((A & mask) << 32) | Q # Retorna o resultado (A é a metade mais significativa e Q, a menos)

    return to_signed(result, 32 * 2)


def division(num1, num2):
    mask = (1 << 32) - 1

    msb_num1 = (num1 >> (32 - 1)) & 1
    msb_num2 = (num2 >> (32 - 1)) & 1

    signed = msb_num1 ^ msb_num2

    if msb_num1:
        num1 = two_complement(num1, 32) & mask

    if msb_num2:
        num2 = two_complement(num2, 32) & mask

    A = 0
    n = 1
    for i in range(0, 32):
        msb_num1 = (num1 >> (32 - 1)) & 1

        A = (A << 1) & mask
        A = A | msb_num1
        num1 = (num1 << 1) & mask

        if is_bigger_than(A, num2, 32):
            A = (A - num2) & mask
            num1 = num1 | 0b1
        else:
            num1 = num1 | 0b0

        n += 1

    if signed:
        num1 = two_complement(num1, 32) & mask
        A = two_complement(A, 32) & mask

    return to_signed(num1, 32), to_signed(A, 32)
