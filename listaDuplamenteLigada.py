class NO:
    def __init__(self, valor):
        self.valor = valor    
        self.proximo = None
        self.anterior = None
        
class listaDuplamenteLigada:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        atual = self.inicio
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo
        
    def inserir_inicio(self, valor):
        novo = NO(valor)
        novo.proximo = self.inicio
        self.inicio = novo
        if novo.proximo is not None:
            novo.proximo.anterior = novo
            
    def inserir_final(self, valor):
        novo = NO(valor)
        if self.inicio is None: self.inicio = novo; return
        atual=self.inicio
        
        while atual.proximo is not None:    
            atual = atual.proximo
        atual.proximo = novo
        novo.anterior = atual

    def inserir_meio(self, valor, posicao):
        if posicao == 0:
            self.inserir_inicio(valor)
            return
        novo = NO(valor)
        atual = self.inicio
        contador = 0
        
        while atual is not None and contador < posicao:
            contador += 1
            anterior = atual
            atual = atual.proximo
            
        if contador == posicao:
            anterior.proximo = novo
            novo.anterior = anterior
            novo.proximo = atual
            if atual is not None:
                atual.anterior = novo

    def remover_inicio(self):
        if self.inicio is not None:
            self.inicio = self.inicio.proximo
            if self.inicio is not None:
                self.inicio.anterior = None

    def remover_final(self):
        if self.inicio is None:
          return
        
        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo
            
        if atual.anterior is not None:
            atual.anterior.proximo = None
        else:
          self.inicio = None 

lista = listaDuplamenteLigada()

lista.inserir_inicio(1)
lista.inserir_final(3)
lista.imprimir()
print("-----------------")
lista.inserir_meio(2,1)
lista.imprimir()
print("-----------------")
lista.remover_inicio()
lista.imprimir()
print("-----------------")
lista.remover_final()
lista.imprimir()
print("-----------------")
lista.remover_final()
lista.imprimir()