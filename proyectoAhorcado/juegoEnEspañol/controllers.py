import sqlite3 as sql

def createDB():
    conn = sql.connect("datosAhorcado.db")
    conn.commit()
    conn.close()
def createTable():
    conn = sql.connect("datosAhorcado.db")
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE datosNivel1 (
            palabra varchar(60),
            caracteres integer(1),
            letrasPalabra varchar(9)
        )

        """
    )
    conn.commit()
    conn.close
if __name__ == "__main__":
   pass