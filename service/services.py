from entities.entity import Entity
from repository.dao_entity import DAOEntity


class TaskValidationError(ValueError):
    """Erro de validação nos dados da tarefa."""


class TaskNotFoundError(LookupError):
    """Erro quando a tarefa não é encontrada."""


class Services:
    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo, descricao):
        if not isinstance(titulo, str) or not titulo.strip():
            raise TaskValidationError(
                "O título é obrigatório e não pode conter apenas espaços em branco."
            )

        titulo_limpo = titulo.strip()
        descricao_limpa = descricao.strip() if isinstance(descricao, str) else ""

        tarefa = Entity(
            titulo=titulo_limpo,
            descricao=descricao_limpa,
            concluida=False,
        )
        tarefa.id = self.repository.create(tarefa)
        return tarefa

    def list(self):
        return self.repository.find_all()

    def get(self, tarefa_id):
        tarefa = self.repository.find_by_id(tarefa_id)
        if not tarefa:
            raise TaskNotFoundError(f"Tarefa com ID {tarefa_id} não encontrada.")
        return tarefa

    def update(self, tarefa_id, titulo, descricao):
        if not isinstance(titulo, str) or not titulo.strip():
            raise TaskValidationError(
                "O título é obrigatório e não pode conter apenas espaços em branco."
            )

        tarefa_existente = self.get(tarefa_id)

        titulo_limpo = titulo.strip()
        descricao_limpa = descricao.strip() if isinstance(descricao, str) else ""

        tarefa_atualizada = Entity(
            id=tarefa_existente.id,
            titulo=titulo_limpo,
            descricao=descricao_limpa,
            concluida=tarefa_existente.concluida,
        )
        self.repository.update(tarefa_atualizada)
        return tarefa_atualizada

    def delete(self, tarefa_id):
        self.get(tarefa_id)
        self.repository.delete(tarefa_id)

    def complete(self, tarefa_id):
        self.get(tarefa_id)
        self.repository.set_concluida(tarefa_id, True)
        return self.get(tarefa_id)