from aula01 import classe_conjunto

c = classe_conjunto("Conjunto01")

c.inserir('A')
c.inserir('Q')
c.inserir('C')
c.inserir('D')
c.imprimir()

d = classe_conjunto("Conjunto02")
d.inserir('A')
d.inserir('Q')
d.inserir('C')
d.inserir('D')
d.inserir('E')
d.inserir('F')
d.imprimir()

print(c.tamanho())
print(c.pertence('A'))
print(c.eh_subconjunto(d))
print(c.contem_propriamente(d))