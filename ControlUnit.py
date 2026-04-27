from RAM import RAM
from CPU import CPU
from MicroProgram import microprogram

class ControlUnit:
    def __init__(self):
        self.MPC = 0
        self.MIC = microprogram
        self.CPU = CPU()
        self.RAM = RAM()

    def set_memory_function(self, code):
        if code & 0b100 != 0:
            self.CPU.MDR = self.RAM.read_word(self.CPU.MAR)

        if code & 0b010 != 0:
            self.RAM.write_word(self.CPU.MAR, self.CPU.MDR)

        if code & 0b001 != 0:
            self.CPU.MBR = self.RAM.read_byte(self.CPU.PC)


    def set_MD_function(self, code):
        if code & 0b001 != 0:
            self.CPU.MDRD = self.RAM.read_word(self.CPU.MARD)

        if code & 0b010 != 0:
            self.RAM.write_word(self.CPU.MARD, self.CPU.MDRD)

        if code & 0b100 != 0:
            self.CPU.MBRD = self.RAM.read_byte(self.CPU.PC)


    def next_address(self, jmpc, jamn, jamz, addr):
        self.MPC = addr #Define, por default, o ADDR da microinstrução como o próximo MPC

        if jmpc:
            self.MPC = addr | (self.CPU.MBR & 0xFF) #"Salta" para a próxima microintrução

        if jamn and self.CPU.N:
            self.MPC = self.MPC | 0x100 #Se o resultado da ALU for negativo, avança 256 endereços

        if jamz and self.CPU.Z:
            self.MPC = self.MPC | 0x100 #Se o resultado da ALU for zero, avança 256 endereços


    def step(self):
        micro_inst = self.MIC[self.MPC]

        if micro_inst == 0:
            return False

        ADDR = (micro_inst >> 31) & 0b111111111
        JMPC = (micro_inst >> 30) & 0b1
        JAMN = (micro_inst >> 29) & 0b1
        JAMZ = (micro_inst >> 28) & 0b1
        ALU = (micro_inst >> 19) & 0b111111111
        C = (micro_inst >> 10) & 0b111111111
        M = (micro_inst >> 7) & 0b111
        B = (micro_inst >> 3) & 0b1111
        MD = micro_inst & 0b111

        a_value = self.CPU.H # Valor A sempre vem do registrador H
        b_value = self.CPU.get_register_value(B)

        left_shift = (ALU >> 8) & 1
        right_shift = (ALU >> 7) & 1
        f2 = (ALU >> 6) & 1
        f1 = (ALU >> 5) & 1
        f0 = (ALU >> 4) & 1
        ENa = (ALU >> 3) & 1
        ENb = (ALU >> 2) & 1
        INVa = (ALU >> 1) & 1
        inc = ALU & 1

        result = self.CPU.alu(a_value, b_value, left_shift, right_shift, f2, f1, f0, ENa, ENb, INVa, inc)

        self.CPU.write_register_value(C, result)

        self.set_memory_function(M)
        self.set_MD_function(MD)

        self.next_address(JMPC, JAMN, JAMZ, ADDR) #Define o endereço da próxima microinstrução


        print(a_value, b_value, left_shift, right_shift, f2, f1, f0, ENa, ENb, INVa, inc)

        if self.MPC == 0:
            print("INIT:")
            print(f"Proximo endereço: {self.MPC}\n")

        if self.MPC >= 0b000000010 and self.MPC <= 0b000000111:
            print("PUSH:", self.MPC)
            print(f"A: {a_value} | B: {b_value} | TOS {self.CPU.TOS}\n")

        if self.MPC >= 0b000001000 and self.MPC <= 0b000001101:
            print("SOMA:", self.MPC)
            print(f"A: {a_value} | B: {b_value} | Result: {result} | TOS {self.CPU.TOS}\n")

        if self.MPC >= 0b000001110 and self.MPC <= 0b000010011:
            print("SUB:", self.MPC)
            print(f"A: {a_value} | B: {b_value} | Result: {result} | TOS {self.CPU.TOS}\n")

        if self.MPC >= 0b000010100 and self.MPC <= 0b000011001:
            print("MUL:", self.MPC)
            print(f"A: {a_value} | B: {b_value} | Result: {result} | TOS {self.CPU.TOS}\n")

        if self.MPC >= 0b000011010 and self.MPC <= 0b000011111:
            print("DIV:", self.MPC)
            print(f"A: {a_value} | B: {b_value} | Result: {result} | TOS {self.CPU.TOS}\n")


        if self.MPC == 0b000100110 or self.MPC == 0b000100111:
            print("MOV:", self.MPC)
            print(f"MBR: {self.CPU.MBR} | MBRD: {self.CPU.MBRD} | PC: {self.CPU.PC} | {self.RAM.read_byte(self.CPU.PC)}\n")

        if self.MPC == 0b100100111:
            print("MOV H:", self.MPC)
            print(f"MBRD: {self.CPU.MBRD}\n")

        if self.MPC == 0b100101000:
            print("MOV OPC:", self.MPC)
            print(f"MBRD: {self.CPU.MBRD}\n")


        return True

