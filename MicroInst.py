class MicroInst:
    def __init__(self, B, C, ALU, M, J, ADDR):
        self.B = B
        self.C: list = C
        self.ALU = ALU
        self.M = M
        self.J = J
        self.ADDR = ADDR