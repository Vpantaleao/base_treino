from database.connection import get_connection
from entities.entity import Entity


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
        connection = get_connection()
        try:
            row = connection.execute(
                """
                SELECT id, titulo, descricao, concluida
                FROM tarefas
                WHERE id = ?
                """,
                (tarefa_id,),
            ).fetchone()

            if not row:
                return None

            return Entity(
                id=row["id"],
                titulo=row["titulo"],
                descricao=row["descricao"],
                concluida=bool(row["concluida"]),
            )
        finally:
            connection.close()

    def update(self, tarefa):
        connection = get_connection()
        try:
            cursor = connection.execute(
                """
                UPDATE tarefas
                SET titulo = ?, descricao = ?
                WHERE id = ?
                """,
                (tarefa.titulo, tarefa.descricao, tarefa.id),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()

    def delete(self, tarefa_id):
        pass