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

micro_program = (MicroInst(0x0001, [0,0,0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [1,0,0], 0b0010),
                 MicroInst(0x0000, [0,0,0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [1,0,0], 0b1000))
