n = int( input( "numero da sequencia = "))
vetor [n] = int(input("Insira o vetor= "))
i = 0
q = 1
while i < n:
    if vetor [i] < vetor [i + 1]:
        q += 1
    i += 1

print q
