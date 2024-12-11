class ContaBancaria:
    def __init__(self, numero_conta, nome_cliente, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.saldo = saldo_inicial
        self.historico = []

    def registrar_transacao(self, tipo, valor):
        self.historico.append(f"{tipo}: R${valor:.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            self.consultar_saldo()
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            self.consultar_saldo()
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            print("Valor de saque inválido.")
    
    def encerrar_conta(self):
        if self.saldo == 0:
            print(f"Conta {self.numero_conta} encerrada com sucesso.")
            return True
        else:
            print("Não é possível encerrar a conta com saldo positivo. Realize um saque ou depósito até que o saldo seja zero.")
            return False
    
    def mostrar_historico(self):
        print(f"Histórico de transações da conta {self.numero_conta}:")
        if not self.historico:
            print("Nenhuma transação realizada.")
        for transacao in self.historico:
            print(transacao)

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, nome_cliente, saldo_inicial=0):
        if numero_conta not in self.contas:
            nova_conta = ContaBancaria(numero_conta, nome_cliente, saldo_inicial)
            self.contas[numero_conta] = nova_conta
            print(f"Conta criada com sucesso para {nome_cliente}. Número da conta: {numero_conta}.")
        else:
            print(f"Erro: A conta {numero_conta} já existe.")

    def consultar_conta(self, numero_conta):
        if numero_conta in self.contas:
            self.contas[numero_conta].consultar_saldo()
        else:
            print(f"Erro: Conta {numero_conta} não encontrada.")

    def realizar_deposito(self, numero_conta, valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].depositar(valor)
        else:
            print(f"Erro: Conta {numero_conta} não encontrada.")

    def realizar_saque(self, numero_conta, valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].sacar(valor)
        else:
            print(f"Erro: Conta {numero_conta} não encontrada.")

    def encerrar_conta(self, numero_conta):
        if numero_conta in self.contas:
            conta = self.contas[numero_conta]
            if conta.encerrar_conta():
                del self.contas[numero_conta]
        else:
            print(f"Erro: Conta {numero_conta} não encontrada.")
    
    def mostrar_historico_conta(self, numero_conta):
        if numero_conta in self.contas:
            self.contas[numero_conta].mostrar_historico()
        else:
            print(f"Erro: Conta {numero_conta} não encontrada.")


banco = Banco()

banco.criar_conta("123", "João", 1000)
banco.criar_conta("124", "Maria", 500)

banco.realizar_deposito("123", 200)
banco.realizar_saque("123", 150)
banco.realizar_saque("124", 600)  
banco.realizar_deposito("124", 200)

banco.consultar_conta("123")
banco.mostrar_historico_conta("123")
banco.mostrar_historico_conta("124")

banco.encerrar_conta("123")
banco.encerrar_conta("124")

banco.consultar_conta("123")