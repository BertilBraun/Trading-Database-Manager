from Utils import *
import argparse

if __name__ == "__main__":
    conn = create_connection()
    
    parser = argparse.ArgumentParser(description='Add Information to DB for the last selling Trade')
    parser.add_argument('-acost', type=float, help='Additional Costs arising for the Trade', default=0)
    parser.add_argument('-pshare', type=float, help='Cost per Share of the Trade', required=True)
    parser.add_argument('-shares', type=float, help='Amount of Shares of the Trade', required=True)
    parser.add_argument('-cost', type=float, help='Combined Cost of the Trade', default=0)
    parser.add_argument('-name', help='The Name of the Stock which was Traded', required=True)

    args = parser.parse_args()
    
    with conn:
    
        cost = args.cost
        if cost == 0:
            cost = round(args.acost + args.pshare * args.shares, 2)
                
        Update(conn, args.acost, args.pshare, -args.shares, -cost, args.name)