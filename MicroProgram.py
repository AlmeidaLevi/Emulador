from array import array

#   ADDR    JAM    ALU        C      M   B
# 000000000 000 000000000 000000000 000 0000

microprogram = array("L", [0]) * 512
#microprogram[0] = 0b000000001000001100011000000000000000 # ADDR & JAM: Passa para a próxima instução; Processo: inicializa o contador (inicia com 1)
#microprogram[1] = 0b000000001001001110011000000000000000 # ADDR & JAM: Dá um "jump" se der overflow (resultado igual a 0), encerrando o processo; Processo: incrementa o contador em 1

microprogram[2] = 0b0000000110000000110000000000001000000 #Coloquei o valor da memoria no MDR

microprogram[3] = 0b0000001000000001100010000000010001010 #MAR = 1

microprogram[4] = 0b0000001010000000101001000000001000000
#Coloca o que tá em MDR no H e coloca MAR no MDR

microprogram[5] = 0b0000001100000000101000010000000000000
#Coloca o que tá em MDR no TOS

microprogram[6] = 0b0000001110000010111000001000000000111 # multiplica H*TOS

microprogram[7] = 0
