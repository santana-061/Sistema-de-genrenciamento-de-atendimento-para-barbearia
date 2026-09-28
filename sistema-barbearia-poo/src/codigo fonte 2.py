from datetime import datetime
from models import Cliente, Barbeiro, Servico, Agendamento

def main():
    clientes = []
    barbeiros = []
    servicos = [
        Servico("Corte de Cabelo", 45.0, 30),
        Servico("Barba", 35.0, 25),
        Servico("Corte + Barba", 70.0, 50)
    ]
    agendamentos = []

    clientes.append(Cliente("Carlos Silva", "(11) 98765-4321", True))
    barbeiros.append(Barbeiro("João Corte", "(11) 91234-5678", "Degradê"))

    while True:
        print("\n=== SISTEMA DE ATENDIMENTO - BARBEARIA ===")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Barbeiro")
        print("3. Listar Serviços Disponíveis")
        print("4. Realizar Agendamento")
        print("5. Listar Agendamentos")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            tel = input("Telefone: ")
            vip = input("É cliente VIP? (s/n): ").lower() == 's'
            clientes.append(Cliente(nome, tel, vip))
            print("✔ Cliente cadastrado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do barbeiro: ")
            tel = input("Telefone: ")
            esp = input("Especialidade: ")
            barbeiros.append(Barbeiro(nome, tel, esp))
            print("✔ Barbeiro cadastrado com sucesso!")

        elif opcao == "3":
            print("\n--- Serviços ---")
            for i, s in enumerate(servicos):
                print(f"{i + 1}. {s.exibir_servico()}")

        elif opcao == "4":
            if not clientes or not barbeiros:
                print("⚠ Cadastre pelo menos um cliente e um barbeiro antes!")
                continue

            print("\n-- Escolha o Cliente --")
            for i, c in enumerate(clientes):
                print(f"{i + 1}. {c.nome}")
            c_idx = int(input("Número do cliente: ")) - 1

            print("\n-- Escolha o Barbeiro --")
            for i, b in enumerate(barbeiros):
                print(f"{i + 1}. {b.nome}")
            b_idx = int(input("Número do barbeiro: ")) - 1

            print("\n-- Escolha o Serviço --")
            for i, s in enumerate(servicos):
                print(f"{i + 1}. {s.exibir_servico()}")
            s_idx = int(input("Número do serviço: ")) - 1

            data_str = input("Data e Hora (AAAA-MM-DD HH:MM): ")
            try:
                data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
                novo_agendamento = Agendamento(clientes[c_idx], barbeiros[b_idx], servicos[s_idx], data_hora)
                agendamentos.append(novo_agendamento)
                print("✔ Agendamento realizado com sucesso!")
            except ValueError:
                print("❌ Formato inválido! Use: AAAA-MM-DD HH:MM (Ex: 2026-06-10 14:30)")

        elif opcao == "5":
            print("\n=== LISTA DE AGENDAMENTOS ===")
            if not agendamentos:
                print("Nenhum agendamento cadastrado.")
            for ag in agendamentos:
                print(ag.resumo_atendimento())

        elif opcao == "6":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()