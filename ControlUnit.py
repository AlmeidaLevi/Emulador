from RAM import RAM
from CPU import CPU
from MicroInst import MicroInst

class ControlUnit:
    def __init__(self, microprogram: MicroInst):
        self.MPC = 0
        self.microprogram = microprogram


    def step(self, cpu: CPU, ram: RAM):
        instr = self.microprogram[self.MPC]

        b_value = getattr(cpu, instr.B)

        result = cpu.alu(instr.ALU, getattr(cpu, "H"), b_value)

        cpu.Z = 1 if result == 0 else 0
        cpu.N = 1 if (result & 0x80000000) != 0 else 0

        for reg in getattr(cpu, instr.C):
            setattr(cpu, reg, result)

        if instr.M == "READ":
            cpu.MDR = ram.read_word(cpu.MAR)
        elif instr.M == "FETCH":
            cpu.MBR = ram.read_byte(cpu.MAR)
        elif instr.M == "WRITE":
            ram.write_word(cpu.MAR, cpu.MDR)

        if instr.J == "NEXT":
            self.MPC += 1
        elif instr.J == "JMP":
            self.MPC = instr.ADDR
        elif instr.J == "IFZ":
            if cpu.Z == 1:
                self.MPC = instr.ADDR
            else:
                self.MPC += 1
        elif instr.J == "IFN":
            if cpu.N == 1:
                self.MPC = instr.ADDR
            else:
                self.MPC += 1
