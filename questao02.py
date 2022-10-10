salCarlos: float
salJoao: float
meses: int

salCarlos = int(input("Coloque o salário de Carlos: "))
salJoao = int(input("Coloque o salário de João: "))

salJoao = salCarlos / 3
meses = 0
while salJoao < salCarlos:
    salCarlos = salCarlos + (salCarlos * 2 / 100)
    salJoao = salJoao + (salJoao * 5 / 100)
    meses = meses + 1

print(f"Serão necessários {meses} meses para João ultrapassar Carlos")





