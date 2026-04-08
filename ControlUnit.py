from RAM import RAM
from CPU import CPU
from MicroProgram import microprogram

class ControlUnit:
    def __init__(self):
        self.MPC = 0
        self.MIC = MicroProgram.microprogram


    def step(self, cpu: CPU, ram: RAM):
        micro_inst = self.MIC[self.MPC]

        if micro_inst == 0:
            return False

        ADDR = (micro_inst >> 27) & 0b11111111
        JMPC = (micro_inst >> 26) & 0b1
        JAMN = (micro_inst >> 25) & 0b1
        JAMZ = (micro_inst >> 24) & 0b1
        ALU = (micro_inst >> 16) & 0b11111111
        C = (micro_inst >> 7) & 0b111111111
        M = (micro_inst >> 4) & 0b111
        B = micro_inst & 0b111111111


        if (M >> 2) & 0b1 != 0:
            cpu.MDR = ram.read_word(cpu.MAR)

        if (M >> 1) & 0b1 != 0:
            cpu.MBR = ram.read_byte(cpu.PC)
        elif M & 0b1 != 0:
            ram.write_word(cpu.MAR, cpu.MDR)

        a_value = cpu.H # Valor A sempre vem do registrador H
        b_value = cpu.get_register_value(B)

        left_shift = (ALU >> 7) & 0b11
        right_shift = (ALU >> 4) & 0b11
        (ALU >> 6) & 0b11
        f1 = (ALU >> 5) & 0b1
        f2 = (ALU >> 4) & 0b1
        ENa = (ALU >> 3) & 0b1
        INVa = (ALU >> 2) & 0b1
        ENb = (ALU >> 1) & 0b1
        inc = ALU & 0b1

        result = cpu.alu(a_value, b_value, left_shift, right_shift, f1, f2, ENa, INVa, ENb, inc)

        cpu.Z = 1 if result == 0 else 0
        cpu.N = 1 if (result & 0x80000000) != 0 else 0

        cpu.write_C_in_register(C, result)

        #Fetch pode ser executado junto com read ou write

        self.MPC = ADDR

        if JMPC:
            self.MPC = ADDR | cpu.MBR

        if JAMZ and cpu.Z:
            self.MPC = self.MPC | 0x100

        elif JAMN and cpu.N:
            self.MPC = self.MPC | 0x100

        cpu.tick()

        return True

