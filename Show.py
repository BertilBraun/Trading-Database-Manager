from Utils import *


if __name__ == "__main__":
    conn = create_connection()
    
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Stocks")
    
    for name, orders in cur.fetchall():
        
        print(f"\n{name}:\n")
    
        cur.execute(f"SELECT * FROM Orders WHERE stock_name == \"{name}\" ")
        
        for e in cur.fetchall():
            print(e)
    
    print("\n\n")
    
    print(GetDescription(conn))