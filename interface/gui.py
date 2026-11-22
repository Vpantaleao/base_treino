from service.services import Services, TaskNotFoundError, TaskValidationError


class UI:
    def __init__(self, services):
        self.services = services

    def _ler_id(self):
        entrada = input("Informe o ID da tarefa: ").strip()
        try:
            tarefa_id = int(entrada)
            if tarefa_id <= 0:
                print("[Erro] O ID deve ser um número inteiro positivo.")
                return None
            return tarefa_id
        except ValueError:
            print("[Erro] ID inválido. Digite um número inteiro.")
            return None

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

    def _listar_tarefas(self):
        print("\n=== Lista de Tarefas ===")
        tarefas = self.services.list()

        if not tarefas:
            print("Nenhuma tarefa cadastrada no momento.")
            return

        for tarefa in tarefas:
            marcador = "[X]" if tarefa.concluida else "[ ]"
            descricao_exibicao = tarefa.descricao if tarefa.descricao else "(Sem descrição)"
            print(
                f"{marcador} ID: {tarefa.id} | "
                f"Título: {tarefa.titulo} | "
                f"Situação: {tarefa.situacao} | "
                f"Descrição: {descricao_exibicao}"
            )

    def _consultar_tarefa_por_id(self):
        print("\n=== Consultar Tarefa por ID ===")
        tarefa_id = self._ler_id()
        if tarefa_id is None:
            return

        try:
            tarefa = self.services.get(tarefa_id)
            descricao_exibicao = tarefa.descricao if tarefa.descricao else "(Sem descrição)"
            print("\n--- Detalhes da Tarefa ---")
            print(f"ID        : {tarefa.id}")
            print(f"Título    : {tarefa.titulo}")
            print(f"Descrição : {descricao_exibicao}")
            print(f"Situação  : {tarefa.situacao}")
            print("--------------------------")
        except TaskNotFoundError as e:
            print(f"[Aviso] {e}")

    def show_principal_menu(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1 - Cadastrar tarefa")
            print("2 - Listar tarefas")
            print("3 - Consultar tarefa por ID")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self._cadastrar_tarefa()
            elif opcao == "2":
                self._listar_tarefas()
            elif opcao == "3":
                self._consultar_tarefa_por_id()
            elif opcao == "0":
                print("Encerrando...")
                break
            else:
                print("[Erro] Opção inválida.")