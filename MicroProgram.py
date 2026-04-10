from array import array

#   ADDR    JAM    ALU        C      M   B
# 000000000 000 000000000 000000000 000 0000

microprogram = array("L", [0]) * 512
microprogram[0] = 0b000000001000001100011000000000000000 # ADDR & JAM: Passa para a próxima instução; Processo: inicializa o contador (inicia com 1)
microprogram[1] = 0b000000001001001110011000000000000000 # ADDR & JAM: Dá um "jump" se der overflow (resultado igual a 0), encerrando o processo; Processo: incrementa o contador em 1

