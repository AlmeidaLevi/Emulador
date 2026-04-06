from RAM import RAM
from CPU import CPU
from MicroProgram import MicroInst
from MicroProgram import micro_program

class ControlUnit:
    def __init__(self, microprogram: tuple[MicroInst]):
        self.MPC = 0
        self.microprogram = microprogram


    def step(self, cpu: CPU, ram: RAM):
        micro_inst = self.microprogram[self.MPC]

        a_value = cpu.H # Valor A sempre vem do registrador H
        b_value = cpu.get_register_value(micro_inst.B)

        ALU = micro_inst.ALU

        result = cpu.alu(a_value, b_value, ALU[0],
                         ALU[1], ALU[2], ALU[3],
                         ALU[4], ALU[5])

        # ALU[6] == SLL8
        if ALU[6] & 0b1:
            result = (result << 8) & 0xFFFFFFFF

        # ALU[7] == SRA1
        if ALU[7] & 0b1:
            result = (result >> 1) & 0xFFFFFFFF

        cpu.Z = 1 if result == 0 else 0
        cpu.N = 1 if (result & 0x80000000) != 0 else 0

        for i, c in enumerate(micro_inst.C):
            if c != 0:
                cpu.write_C_in_register(i, result)

        #Fetch pode ser executado junto com read ou write
        if micro_inst.M[0] != 0:
            cpu.MDR = ram.read_word(cpu.MAR)

        if micro_inst.M[1] != 0:
            cpu.MBR = ram.read_byte(cpu.MAR)
        elif micro_inst.M[2] != 0:
            ram.write_word(cpu.MAR, cpu.MDR)


        self.MPC = micro_inst.ADDR

        if micro_inst.JAM[0] != 0:
            self.MPC = micro_inst.ADDR | cpu.MBR

        if micro_inst.JAM[1] != 0 and cpu.Z:
            self.MPC = self.MPC | 0x80
        elif micro_inst.JAM[2] != 0 and cpu.N:
            self.MPC = self.MPC | 0x80

        cpu.tick()

