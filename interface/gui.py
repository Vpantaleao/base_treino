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

    def _atualizar_tarefa(self):
        print("\n=== Atualizar Tarefa ===")
        tarefa_id = self._ler_id()
        if tarefa_id is None:
            return

        try:
            tarefa_atual = self.services.get(tarefa_id)
            print(
                f"Atualizando tarefa #{tarefa_atual.id} "
                f"(Situação atual: {tarefa_atual.situacao})"
            )
            novo_titulo = input("Novo título (obrigatório): ")
            nova_descricao = input("Nova descrição (opcional): ")

            tarefa = self.services.update(tarefa_id, novo_titulo, nova_descricao)
            print(
                f"[Sucesso] Tarefa #{tarefa.id} atualizada! "
                f"Situação preservada: {tarefa.situacao}"
            )
        except TaskNotFoundError as e:
            print(f"[Aviso] {e}")
        except TaskValidationError as e:
            print(f"[Erro] {e}")

    def _excluir_tarefa(self):
        print("\n=== Excluir Tarefa ===")
        tarefa_id = self._ler_id()
        if tarefa_id is None:
            return

        try:
            tarefa = self.services.get(tarefa_id)
            descricao_exibicao = tarefa.descricao if tarefa.descricao else "(Sem descrição)"
            print("\n--- Tarefa Selecionada ---")
            print(f"ID        : {tarefa.id}")
            print(f"Título    : {tarefa.titulo}")
            print(f"Descrição : {descricao_exibicao}")
            print(f"Situação  : {tarefa.situacao}")
            print("---------------------------")

            confirmacao = input("Confirma a exclusão permanente? (s/N): ").strip().lower()
            if confirmacao in ("s", "sim"):
                self.services.delete(tarefa_id)
                print(f"[Sucesso] Tarefa #{tarefa_id} excluída permanentemente.")
            else:
                print("[Cancelado] Exclusão cancelada. Nenhuma alteração foi feita.")
        except TaskNotFoundError as e:
            print(f"[Aviso] {e}")

    def show_principal_menu(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1 - Cadastrar tarefa")
            print("2 - Listar tarefas")
            print("3 - Consultar tarefa por ID")
            print("4 - Atualizar tarefa")
            print("5 - Excluir tarefa")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self._cadastrar_tarefa()
            elif opcao == "2":
                self._listar_tarefas()
            elif opcao == "3":
                self._consultar_tarefa_por_id()
            elif opcao == "4":
                self._atualizar_tarefa()
            elif opcao == "5":
                self._excluir_tarefa()
            elif opcao == "0":
                print("Encerrando...")
                break
            else:
                print("[Erro] Opção inválida.")