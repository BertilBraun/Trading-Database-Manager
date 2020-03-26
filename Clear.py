from Utils import *


if __name__ == "__main__":

    create_backup();
    conn = create_connection()
    
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM Stocks")
        cur.execute("DELETE FROM Orders")
        cur.execute("DELETE FROM sqlite_sequence")
    