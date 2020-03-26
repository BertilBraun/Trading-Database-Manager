import sqlite3
from sqlite3 import Error
from shutil import copyfile
 
path = r"C:\Users\Braun\OneDrive\Projects\Trading\Database\Trading.db"

def create_connection():

    try:
        return sqlite3.connect(path)
    except Error as e:
        print(e)
        return None
        
def create_backup():
    copyfile(path, "Trading.backup.db")    

def Update(conn, additional_costs, price_per_share, shares, cost, stock_name):
    
    cur = conn.cursor()
    
    try:
        cur.execute(f"INSERT INTO Stocks (name, owned) VALUES (\"{stock_name}\", 0)")
    except Error as e:
        pass
        
    cur.execute(f"""INSERT INTO Orders 
                        (additional_costs, price_per_share, shares, cost, stock_shares, stock_name) 
                     VALUES 
                         (
                            {additional_costs}, 
                            {price_per_share}, 
                            {shares}, 
                            {cost}, 
                            (SELECT owned FROM Stocks WHERE name == \"{stock_name}\"),
                            \"{stock_name}\")""")
                            
    cur.execute(f"UPDATE Stocks SET owned = (owned + {shares}) WHERE name = \"{stock_name}\"")
    
def Print(conn, table):

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
 
    rows = cur.fetchall()
 
    print(f"\n{table}:\n")
    
    for row in rows:
        print(row)

def GetDescription(conn):
    
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Stocks")
    
    descriptions = []
    
    for name, orders in cur.fetchall():
        
        cur.execute(f"SELECT * FROM Orders WHERE stock_name == \"{name}\" ")
        
        dates = []
        prices = []
        shares = []
        costs = []
        open_shares = []
        
        for e in cur.fetchall(): #(10, '2020-03-26 20:14:37', 7.9, 8.6, -58.0, -502.63, 290.0, 'PO0')
            
            dates.append(e[1])
            prices.append(e[3])
            shares.append(e[4])
            costs.append(e[5])
            open_shares.append(e[6])

        #print(dates)
        #print(prices)
        #print(shares)
        #print(costs)
        #print(open_shares)
        
        shares_open = open_shares[-1] + shares[-1]
        value_of_shares_open = shares_open * prices[-1]
        diff = -sum(costs) + value_of_shares_open
        
        descriptions.append(f"\n{name}: Open Shares: {shares_open}, with a Value of about: {round(value_of_shares_open, 2)}€ and a difference of: {round(diff, 2)}€")
    
    return descriptions
 
if __name__ == "__main__":
    conn = create_connection()
    
    with conn:
    
        Print(conn, "Stocks")
        Print(conn, "Orders")
        
        Update(conn, 7.90, 8.60, 58, 502.63, 'PO0')
        
        Print(conn, "Stocks")
        Print(conn, "Orders")
        
        Update(conn, 3.90, 7.42, -58, -426.53, 'PO0')
        
        Print(conn, "Stocks")
        Print(conn, "Orders")