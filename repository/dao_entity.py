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
        connection = get_connection()
        try:
            rows = connection.execute(
                """
                SELECT id, titulo, descricao, concluida
                FROM tarefas
                ORDER BY id ASC
                """
            ).fetchall()

            return [
                Entity(
                    id=row["id"],
                    titulo=row["titulo"],
                    descricao=row["descricao"],
                    concluida=bool(row["concluida"]),
                )
                for row in rows
            ]
        finally:
            connection.close()

    def find_by_id(self, tarefa_id):
        pass

    def update(self, tarefa):
        pass

    def delete(self, tarefa_id):
        pass