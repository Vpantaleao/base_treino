from service.services import Services, TaskValidationError


class UI:
    def __init__(self, services):
        self.services = services

    def _cadastrar_tarefa(self):
        print("\n=== Cadastrar Tarefa ===")
        titulo = input("Título (obrigatório): ")
        descricao = input("Descrição (opcional): ")

        try:
            tarefa = self.services.create(titulo, descricao)
            print(
                f"[Sucesso] Tarefa cadastrada! ID: {tarefa.id} | "
                f"Situação: {tarefa.situacao}"
            )
        except TaskValidationError as e:
            print(f"[Erro] {e}")

    def show_principal_menu(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1 - Cadastrar tarefa")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self._cadastrar_tarefa()
            elif opcao == "0":
                print("Encerrando...")
                break
            else:
                print("[Erro] Opção inválida.")