def to_signed(value, bits): #Garante que o valor mantenha o sinal
    if value & (1 << (bits - 1)):
        return value - (1 << bits)
    return value

def booth_multiply(A, Q, M, Q_1, n, bits):
    mask = (1 << bits) - 1 #Números só podem ter um único tamanho

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