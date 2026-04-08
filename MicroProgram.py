from array import array

# ADDR endereço da proxima microinstrução
# JAM, lista de 3 bits, [JPMC, JAMZ, JAMN]
# ALU, lista de 8 bits, [f1, f2, ENa, ENb, INVa, INC, SLL8, SRA1]
# C lista de 8 bits que escolhe um registrador pra mandar o resultado da ULA,
# [MAR, MDR, PC, SP, LV, CPP, TOS, OPC, H]
# M lista de 3 bits, [fetch, read, write]
# B "endereço" do registrador a ser lido pra pegar o valor B pra ULA
"""
class MicroInst:
    def __init__(self, ADDR: int, JAM: list[int], ALU: list[int], C: list[int], M: list[int], B: int):
        self.B = B & 0b1111
        self.ADDR = ADDR & 0b111111111
        self.ALU = ALU
        self.C = C
        self.M = M
        self.JAM = JAM

        for i in range(len(self.ALU)):
            self.ALU[i] = ALU[i] & 0b1

        for i in range(len(self.C)):
            self.C[i] = C[i] & 0b1

        for i in range(len(self.C)):
            self.M[i] = M[i] & 0b1

        for i in range(len(self.C)):
            self.JAM[i] = JAM[i] & 0b1
"""

microprogram = array("L", [0]) * 512
microprogram[0] = 0b000000001100000100101000000001000000
microprogram[1] = 0b000000010100001110100000000101000000
microprogram[2] = 0b000000011100000100100000000001000000
