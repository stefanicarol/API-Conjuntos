class classe_conjunto():
    def __init__(self, nome):
        self.elementos = []
        self.nome = nome
        self.quant = 0

    def inserir(self, valor):
        if valor in self.elementos:
            pass
        self.elementos.append(valor)
        self.quant += 1

    def imprimir(self):
        for i in range(self.quant):
            if i == 0:
                print(self.nome, ":{", self.elementos[i], ",", end="")
            elif i + 1 != self.quant:
                print(self.elementos[i], ",", end="")
            else:
                print(self.elementos[self.quant - 1], "}")

    def tamanho(self):
        return len(self.elementos)

    def pertence(self, valor):
        if valor in self.elementos:
            return True

    def eh_subconjunto(self, conjunto):
        for i in conjunto.elementos:
            if i in self.elementos:
                return True
            else:
                return False
        pass

    def contem_propriamente(self, conjunto):
        if len(conjunto.elementos) >= len(self.elementos):
            return False
        else:
            for i in conjunto.elementos:
                if i in self.elementos:
                    pass
                else:
                    return False
                return True