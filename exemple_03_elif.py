# else é opcional, só dá pra ter elif se tiver if

autor = str("~ danielxd")

x = int(input("Informe o valor de x, que seja de 1 a 3, vamos apenas repetir o que você inserir: "))

if x == 0:
    print("0 não estava na lista, animal. >:|")
elif x == 1:
    print("Seu número é 1. :D")
elif x == 2:
    print("Seu número é 2. :D")
elif x == 3:
    print("Seu número é 3. :D")
else:
    print("Bobão, eu não disse para digitar um número fora de 1 a 5!")

print("Fim! :D")

