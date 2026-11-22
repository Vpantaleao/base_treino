from database.connection import get_connection


class DAOEntity:
    def create(self, tarefa):
        connection = get_connection()
        try:
            cursor = connection.execute(
                """
                INSERT INTO tarefas (titulo, descricao, concluida)
                VALUES (?, ?, ?)
                """,
                (tarefa.titulo, tarefa.descricao, int(tarefa.concluida)),
            )
            connection.commit()
            return int(cursor.lastrowid)
        finally:
            connection.close()

    def find_all(self):
        pass

    def find_by_id(self, tarefa_id):
        pass

    def update(self, tarefa):
        pass

    def delete(self, tarefa_id):
        pass