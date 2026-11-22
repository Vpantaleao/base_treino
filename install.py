from database.connection import get_connection


def install():
    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL DEFAULT '',
                concluida INTEGER NOT NULL DEFAULT 0
            )
            """
        )

        cursor = connection.execute("SELECT COUNT(*) FROM tarefas")
        if cursor.fetchone()[0] == 0:
            connection.executemany(
                """
                INSERT INTO tarefas (titulo, descricao, concluida)
                VALUES (?, ?, ?)
                """,
                [
                    ("Configurar ambiente do projeto", "Preparar base SQLite e RF01", 0),
                    ("Revisar requisitos RF01 a RF07", "Validar regras de negócio no terminal", 0),
                ],
            )

        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")