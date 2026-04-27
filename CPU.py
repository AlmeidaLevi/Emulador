import Operations

class CPU:
        def __init__(self):
            self.MAR = 0
            self.MDR = 0
            self.PC = 0
            self.MBR = 0
            self.SP = 0xDFFFF
            self.LV = 0
            self.CPP = 0
            self.TOS = 0
            self.OPC = 0
            self.MARD = 0
            self.MDRD = 0
            self.MBRD = 0
            self.H = 0
            self.Z = 0
            self.N = 0

        def alu(self, a, b, left_shift, right_shift, f2, f1, f0, ENa, ENb, INVa, inc):

            a = (a & 0xFFFFFFFF) if ENa == 1 else 0
            a = a if INVa == 0 else ~a

            b = (b & 0xFFFFFFFF) if ENb == 1 else 0
            result = 0

            if f2 == 0:
                if f1 == 0 and f0 == 0: #AND
                    result = a & b

                elif f1 == 0 and f0 == 1: #OR
                    result = a | b

                elif f1 == 1 and f0 == 0: #NOT_b
                    result = ~b


                elif f1 == 1 and f0 == 1: #SUM
                    result = (a + b + inc) & 0xFFFFFFFF
            else:
                if f1 == 0 and f0 == 0: #XOR
                    result = a ^ b

                elif f1 == 0 and f0 == 1: #a * b (MULTIPLY)
                    result = Operations.booth_multiply(a, b)

                elif f1 == 1 and f0 == 0: #a // b (INTEGER DIVISION)
                    print(a, b)
                    result = Operations.division(b, a)[0]

                elif f1 == 1 and f0 == 1: #a % b (MOD)
                    result = Operations.division(b, a)[1]

            self.Z = 1 if result == 0 else 0
            self.N = 1 if (result & 0x80000000) != 0 else 0

            if left_shift == 1:
                result = (result << 8) & 0xFFFFFFFF

            if right_shift == 1:
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

            if code == 0b1001:
                return self.MDRD

            if code == 0b1010:
                return self.MBRD


            return 0

        def write_register_value(self, code, value):
            """Recebe um valor do barramento C que é escrito em um ou mais dos registradores.
            Os registradores que recebem o valor são selecionados a partir do código (code) dado pela Unidade de Controle"""

            if code & 0b000000001:
                self.MAR = value

            if code & 0b000000010:
                self.MDR = value

            if code & 0b000000100:
                self.PC = value

            if code & 0b000001000:
                self.SP = value

            if code & 0b000010000:
                self.LV = value

            if code & 0b000100000:
                self.CPP = value

            if code & 0b001000000:
                self.TOS = value

            if code & 0b010000000:
                self.OPC = value

            if code & 0b100000000:
                self.H = value
