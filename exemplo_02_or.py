x = int(input("Devo trocar o óleo? Fazem quantos meses desde a última troca? "))
y = int(input("Quantos km você já dirigiu desde a última troca? "))

if x >= 6 or y >= 10000:
    print("Sim. Deve trocar o óleo. :D")
else:
    print("Ainda não precisa. :D")

print("*** FIM ***")

#else é sempre opcional