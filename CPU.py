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

        def alu(self, f1, f2, a, b, ENa, ENb, INVa, inc):
            f1 = f1 & 0b1
            f2 = f2 & 0b1
            ENa = ENa & 0b1
            ENb = ENb & 0b1
            INVa = INVa & 0b1
            inc = inc & 0b1

            a = (a & 0xFFFFFFFF) if ENa == 1 else 0
            a = a if INVa == 0 else ~a

            b = (b & 0xFFFFFFFF) if ENb == 1 else 0

            if f1 | f2 == 0:
                return a & b

            if f1 == 0 and f2 == 1:
                return a | b

            if (f1 & f2) == 1:
                return a + b + inc

            return ~b

        def get_register_value(self, code):
            if code == 0b0000:
                return self.MDR

            if code == 0b0001:
                return self.PC

            if code == 0b0010:
                self.MBR & 0xFF

                if self.MBR & 0x80:
                    return self.MBR | 0xFFFFFF00
                return self.MBR

            if code == 0b0011:
                return self.MBR & 0xFF

            if code == 0b0100:
                return self.SP

            if code == 0b0101:
                return self.LV

            if code == 0b0110:
                return self.CPP

            if code == 0b0111:
                return self.TOS

            if code == 0b1000:
                return self.OPC

            return 0
