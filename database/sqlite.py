import sqlite3


class DbClass:

    def __init__(self, path: str) -> None:
        self.path = path

    def execute(self, code: str, fetch: str = None):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()

        cursor.execute(code)

        conn.close()

        if fetch == "all":
            return cursor.fetchall()

        elif fetch == "one":
            return cursor.fetchone()

        elif fetch == "many":
            return cursor.fetchmany()

        else:
            return 0

    def execute_args(self, code: str, args: tuple, fetch: str = None):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()

        cursor.execute(code, args)

        conn.close()

        if fetch == "all":
            return cursor.fetchall()

        elif fetch == "one":
            return cursor.fetchone()

        elif fetch == "many":
            return cursor.fetchmany()

        else:
            return 0