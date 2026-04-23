from ControlUnit import ControlUnit
import Clock

dev = ControlUnit()

#dev.RAM.memory[0] = 0b00000000000000000000000000000111 # 7
#dev.RAM.memory[1] = 0b11111111111111111111111111111110 # -2 em complemento de 2

#dev.MPC = 2

ticks = Clock.start([dev], False)

print(dev.RAM.memory[1])
print(ticks)
