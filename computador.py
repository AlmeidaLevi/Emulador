from ControlUnit import ControlUnit
import Clock

dev = ControlUnit()


#ADD
# dev.RAM.write_byte(1, 0b000000010)
# dev.RAM.write_byte(2, 100)
# dev.RAM.write_byte(3, 0b000000010)
# dev.RAM.write_byte(4, 101)
# dev.RAM.write_byte(5, 0b000001000)
# dev.RAM.write_byte(6, 0b100101110)



#MOV
dev.RAM.write_byte(1, 0b000101010)
dev.RAM.write_byte(2, 0)
dev.RAM.write_byte(3, 0)
dev.RAM.write_byte(4, 20)
dev.RAM.write_byte(5, 1)

print(dev.RAM.memory[4])
ticks = Clock.start([dev], True)

print((dev.CPU.OPC))

print(ticks)
