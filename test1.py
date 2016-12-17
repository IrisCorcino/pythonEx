intervalo = int( input( "Interval = "))
cont = 1
quant = 0
while  cont <= intervalo :
    cont2 = 1
    soma = 0
    while cont2 < cont:
        resto = cont % cont2
        if resto == 0:
            soma += cont2
        cont2 += 1
    if soma == cont:
        quant += 1
        print cont
    cont += 1

print "Amount of perfect numers is %i " % quant
