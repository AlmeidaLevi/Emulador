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
            self.CPU.PC += 1

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

        ADDR = (micro_inst >> 28) & 0b111111111
        JMPC = (micro_inst >> 27) & 0b1
        JAMN = (micro_inst >> 26) & 0b1
        JAMZ = (micro_inst >> 25) & 0b1
        ALU = (micro_inst >> 16) & 0b111111111
        C = (micro_inst >> 7) & 0b111111111
        M = (micro_inst >> 4) & 0b111
        B = micro_inst & 0b1111

        a_value = self.CPU.H # Valor A sempre vem do registrador H
        b_value = self.CPU.get_register_value(B)

        left_shift = (ALU >> 8) & 1
        right_shift = (ALU >> 7) & 1
        f2 = (ALU >> 6) & 1
        f1 = (ALU >> 5) & 1
        f0 = (ALU >> 4) & 1
        ENa = (ALU >> 3) & 1
        INVa = (ALU >> 2) & 1
        ENb = (ALU >> 1) & 1
        inc = ALU & 1

        result = self.CPU.alu(a_value, b_value, left_shift, right_shift, f2, f1, f0, ENa, INVa, ENb, inc)

        print(result)

        self.CPU.write_register_value(C, result)

        self.set_memory_function(M)

        self.next_address(JMPC, JAMN, JAMZ, ADDR) #Define o endereço da próxima microinstrução

        return True

