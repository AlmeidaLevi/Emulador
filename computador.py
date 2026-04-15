from ControlUnit import ControlUnit
import Clock

dev = ControlUnit()

dev.RAM.memory[0] = 0b00000000000000000000000000000100 # 4
dev.RAM.memory[1] = 0b11111111111111111111111111111110 # -2 em complemento de 2


dev.RAM.write_byte(0, 2)

Clock.start([dev], False)

