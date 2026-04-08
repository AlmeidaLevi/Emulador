from RAM import RAM

class CPU:
        def __init__(self):
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

        def alu(self, a, b, left_shift, right_shift, f1, f2, ENa, ENb, INVa, inc):

            a = (a & 0xFFFFFFFF) if ENa == 1 else 0
            a = a if INVa == 0 else ~a

            b = (b & 0xFFFFFFFF) if ENb == 1 else 0

            if f1 | f2 == 0:
                result = a & b

            elif f1 == 0 and f2 == 1:
                result = a | b

            elif (f1 & f2) == 1:
                result = (a + b + inc) & 0xFFFFFFFF

            else:
                result = ~b

            # ALU[6] == SLL8
            if left_shift == 1:
                result = (result << 8) & 0xFFFFFFFF

            # ALU[7] == SRA1
            if right_shift == 0b01:
                result = (result >> 1) & 0xFFFFFFFF

            return result

        def get_register_value(self, code):
            if code == 0b0000:
                return self.MDR

            if code == 0b0001:
                return self.PC

            if code == 0b0010:
                self.MBR = self.MBR & 0xFF

                if self.MBR & 0x100:
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

        def write_C_in_register(self, code, value):
            if code & 0b1:
                self.MAR = value
                return

            if (code >> 1) & 0b1:
                self.MDR = value
                return

            if (code >> 2) & 0b1:
                self.PC = value
                return

            if (code >> 3) & 0b1:
                self.SP = value
                return

            if (code >> 4) & 0b1:
                self.LV = value
                return

            if (code >> 5) & 0b1:
                self.CPP = value
                return

            if (code >> 6) & 0b1:
                self.TOS = value
                return

            if(code >> 7) & 0b1:
                self.OPC = value
                return

            if (code >> 8) & 0b1:
                self.H = value
                return

            return
