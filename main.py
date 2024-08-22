class Pilha:
    def __init__(self, max_size):
        self.pilha = []
        self.max_size = max_size

    def push(self, item):
        if len(self.pilha) < self.max_size:
            self.pilha.append(item)
            print(f"Item {item} adicionado à pilha.")
        else:
            print("Erro: a pilha está cheia. Não pode mais colocar itens :( ")

    def pop(self):
        if not self.is_empty():
            item = self.pilha.pop()
            print(f"Item {item} removido da pilha.")
        else:
            print("Erro! Não é possível remover item.")

    def peek(self):
        if not self.is_empty():
            return self.pilha[-1]
        else:
            print("Erro! A pilha está vazia.")
            return None

    def is_empty(self):
        return len(self.pilha) == 0
    
    def __str__(self):
        return f"Pilha atual: {self.pilha}"
    
def main():
    max_size = int(input("Digite o tamanho máximo da pilha: "))
    pilha = Pilha(max_size)

    while True:
        print("\nMenu")
        print("1. Push (adicionar)")
        print("2. Pop (remover)")
        print("3. Peek (topo da lista)")
        print("4. Sair")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            item = input("Digite o elemento que vai ser adicionado: ")
            pilha.push(item)
        elif escolha == 2:
            pilha.pop()
        elif escolha == 3:
            topo = pilha.peek()
            if topo is not None:
                print(f"Elemento no topo da pilha: '{topo}'")
        elif escolha == 4:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")
        print(pilha)

if __name__ == "__main__":
    main()
