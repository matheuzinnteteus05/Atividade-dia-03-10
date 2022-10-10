from datetime import datetime

salInicial: float
anoInicial: int
anoAtual: int
aumento: float
novoSal: float

salInicial = 1000
anoInicial = 2005
anoAtual = datetime.today().year
aumento = 1.5 * 1000
novoSal = 3 * 1000

while anoInicial < anoAtual:
    anoInicial += 1
    salInicial = 1 + aumento
    aumento = 2

print(f"O salário em {anoAtual} é de R$ {novoSal:2f} ")
