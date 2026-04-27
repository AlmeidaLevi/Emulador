from ControlUnit import ControlUnit
import Clock

dev = ControlUnit()

dev.RAM.memory[100] = 10
dev.RAM.memory[101] = 15

#ADD
# dev.RAM.write_byte(1, 0b000000010)
# dev.RAM.write_byte(2, 100)
# dev.RAM.write_byte(3, 0b000000010)
# dev.RAM.write_byte(4, 101)
# dev.RAM.write_byte(5, 0b000001000)
# dev.RAM.write_byte(6, 0b100101110)

#MOV
dev.RAM.write_byte(1, 0b00100110)
dev.RAM.write_byte(2, 0b00101000)
dev.RAM.write_byte(3, 0)
dev.RAM.write_byte(4, 25)
dev.RAM.write_byte(5, 1)


ticks = Clock.start([dev], True)

print(dev.CPU.OPC)

print(ticks)
