import json
from web3 import Web3
from tkinter import *
#make sure to pip install web3[tester] on the shell

w3 = Web3(Web3.EthereumTesterProvider())

root=Tk()
root.resizable(False,False)
root.geometry('130x195')
root.title(' ')

err=Label(root,text='',font=('Arial',8),fg='Red')
err.place(x=8,y=173)

def send(a,b,c):
  if int(a)==int(b):
    err.place(x=16,y=173)
    err.config(text='Change recipient')
    err.config(fg='Red')
  elif c=='':
    err.config(text='Amount field empty')
    err.config(fg='Red')
    err.place(x=8,y=173)
  else:
    err.config(text='Sent successfuly!')
    err.config(fg='Green')
    err.place(x=16,y=173)
    tx_hash = w3.eth.send_transaction({
    'from': w3.eth.accounts[int(a)],
    'to': w3.eth.accounts[int(b)],
    'value': w3.toWei(int(c), 'ether')})

  print(w3.eth.get_balance(w3.eth.accounts[0]))
  print(w3.eth.get_balance(w3.eth.accounts[1]))
  print(w3.eth.get_balance(w3.eth.accounts[2]))
  print(w3.eth.get_balance(w3.eth.accounts[3]))
  print(w3.eth.get_balance(w3.eth.accounts[4]))
  print(w3.eth.get_balance(w3.eth.accounts[5]))

var = StringVar()
var.set("0")

var2 = StringVar()
var2.set("0")

fromm=Label(root,text='From:').place(x=5,y=5)
frommm=OptionMenu(root,var, "0", "1", "2","3", "4", "5").place(x=60,y=3)

too=Label(root,text='To:').place(x=5,y=45)
tooo=OptionMenu(root,var2, "0", "1", "2","3", "4", "5").place(x=60,y=45)

amm=Label(root,text='Amount:').place(x=5,y=90)
ammm=Entry(root,width=12)
ammm.place(x=5,y=108)

submitt=Button(root,text='Submit',command=lambda:send(var.get(),var2.get(),ammm.get())).place(x=25,y=137)

#check the console

root.mainloop()
