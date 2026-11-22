from entities.entity import Entity
from repository.dao_entity import DAOEntity


class TaskValidationError(ValueError):
    """Erro de validação nos dados da tarefa."""


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
        pass

    def get(self, tarefa_id):
        pass

    def update(self, tarefa_id, titulo, descricao):
        pass

    def delete(self, tarefa_id):
        pass