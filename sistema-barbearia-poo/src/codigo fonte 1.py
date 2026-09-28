from abc import ABC, abstractmethod
from datetime import datetime

# 1. ABSTRAÇÃO E HERANÇA
class Pessoa(ABC):
    def __init__(self, nome, telefone):
        self._nome = nome          # Encapsulamento
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @abstractmethod
    def exibir_dados(self):
        pass

class Cliente(Pessoa):
    def __init__(self, nome, telefone, fidelidade=False):
        super().__init__(nome, telefone)
        self.fidelidade = fidelidade

    def exibir_dados(self):
        status_vip = "Sim" if self.fidelidade else "Não"
        return f"[Cliente] Nome: {self.nome} | Telefone: {self.telefone} | VIP: {status_vip}"

class Barbeiro(Pessoa):
    def __init__(self, nome, telefone, especialidade):
        super().__init__(nome, telefone)
        self.especialidade = especialidade

    def exibir_dados(self):
        return f"[Barbeiro] Nome: {self.nome} | Telefone: {self.telefone} | Especialidade: {self.especialidade}"

# 2. CLASSES DE NEGÓCIO
class Servico:
    def __init__(self, descricao, preco, duracao_min):
        self.descricao = descricao
        self.preco = preco
        self.duracao_min = duracao_min

    def exibir_servico(self):
        return f"{self.descricao} - R$ {self.preco:.2f} ({self.duracao_min} min)"

class Agendamento:
    def __init__(self, cliente, barbeiro, servico, data_hora):
        self.cliente = cliente
        self.barbeiro = barbeiro
        self.servico = servico
        self.data_hora = data_hora

    def resumo_atendimento(self):
        data_formatada = self.data_hora.strftime('%d/%m/%Y às %H:%M')
        return (
            f"----------------------------------------\n"
            f"Data/Hora: {data_formatada}\n"
            f"-> {self.cliente.exibir_dados()}\n"
            f"-> {self.barbeiro.exibir_dados()}\n"
            f"-> Serviço: {self.servico.exibir_servico()}\n"
            f"----------------------------------------"
        )