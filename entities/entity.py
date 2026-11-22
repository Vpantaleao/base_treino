class Entity:
    def __init__(
        self,
        titulo: str,
        descricao: str = "",
        concluida: bool = False,
        id: int | None = None,
    ):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    @property
    def situacao(self) -> str:
        return "Concluída" if self.concluida else "Pendente"