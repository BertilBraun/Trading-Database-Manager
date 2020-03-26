import PySimpleGUI as sg
from Utils import *
import os

sg.theme('DarkAmber')

#additional_costs, price_per_share, shares, cost, stock_name

name = sg.InputText(key="stock_name")
pps = sg.Input("0", key="price_per_share")
shares = sg.Input("0", key="shares")
cost = sg.Input("0", key="cost")
acost = sg.Input("0", key="additional_costs")

def Reset():         
    acost.Update("0")
    pps.Update("0")
    shares.Update("0")
    cost.Update("0")
    name.Update("")

layout = [  [sg.Text('Enter a new Trade to the Database'), sg.Combo(['Buy', 'Sell'], "Buy", key="buy_sell")],
            [sg.Text('Stock Name: '), name],
            [sg.Text('Price per Share: '), pps],
            [sg.Text('Amount of Shares: '), shares],
            [sg.Text('Combined Costs: '), cost],
            [sg.Text('Additional Costs: '), acost],
            [sg.Submit(), sg.Cancel()] ]
         
window = sg.Window('Trading Database', layout)
 
while True:
    event, values = window.read()
    
    if event in (None, 'Cancel'):
        break
    
    if event == "Submit":
           
        def Get(e):
            return e.Get().replace(',', '.')
        
        path = r"C:\Users\Braun\OneDrive\Projects\Trading\\" + values["buy_sell"] + ".py "
        params = f'-acost {Get(acost)} -pshare {Get(pps)} -shares {Get(shares)} -cost {Get(cost)} -name {name.Get().upper()}' 
               
        os.system('python ' + path + params)
        
        sg.Window('Trading Overview', [ [sg.Text(''.join(GetDescription(create_connection())))] ]).Read()

window.close()