# Emulador

# Mapeamento da memoria:

Espaço pra programa:
0x00001 - 0x80000

Espaço das local variables
0x80001 - 0x80100

Espaço da constant pool
0x80101 - undefined

Espaço da stack:
0xDFFFF - 0xFFFFF

# Instruções
OPCODES:

PUSH: 0b000000010

SUM_STACK:  0b000001000

SUB_STACK:  0b000001110

MUL_STACK:  0b000010100

DIV_STACK:  0b000011010

MOD-STACK:  0b000100000

MOV:  0b000100110

STORE_LOCAL: 0b000101010

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

