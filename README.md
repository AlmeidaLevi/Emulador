# Emulador

# Mapeamento da memoria:

Espaço pra programa:
0x00001 - 0x80000

Espaço da stack:
start: 0xDFFFF
finish: 0xFFFFF

# Instruções
OPCODES:

PUSH: 0b000000010

ADD:  0b000001000

SUB:  0b000001110

MUL:  0b000010100

DIV:  0b000011010

MOD:  0b000100000

MOV:  0b000100110

# Registradores barramento B
MDR           = 0000
PC            = 0001
MBR(unsigned) = 0010
MBR           = 0011
SP            = 0100
LV            = 0101
CPP           = 0110
TOS           = 0111
OPC           = 1000
MDRD          = 1001
MBRD          = 1010

