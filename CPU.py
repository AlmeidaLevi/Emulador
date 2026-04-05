from RAM import RAM

class CPU:
        def __init__(self, ram: RAM):
            self.cycles = 0
            self.MAR = 0
            self.MDR = 0
            self.PC = 0
            self.MBR = 0
            self.SP = 0
            self.LV = 0
            self.CPP = 0
            self.TOS = 0
            self.OPC = 0
            self.H = 0
            self.Z = 0
            self.N = 0

        def tick(self):
            self.cycles += 1

        def alu(self, op, a, b):
            if op == 'AND':
                return (a + b) & 0xFFFFFFFF
            elif op == 'OR':
                return (a | b) & 0xFFFFFFFF
            elif op == 'NOT':
                return (~a) & 0xFFFFFFFF
            elif op == 'PASS':
                return (a ^ b) & 0xFFFFFFFF
            else:
                exit(0)
