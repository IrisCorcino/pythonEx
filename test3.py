n = int (input("Digite um numero menor que 10 = "))

aux, reverso= n, 0


while aux != 0:
    reverso = reverso * 10 +  aux % 10
    aux //= 10

if reverso == n:
    print " %i eh numero do exercicio " % n
else :
    print "Nao eh palidromo"
