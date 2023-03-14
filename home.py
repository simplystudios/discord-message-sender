import time
import requests
from tkinter import *

root = Tk()
root.geometry("360x180")
root.configure(bg='teal')

mylabel = Label(root, text="DC PINGER 1.0", fg='orange', font=40, bg='teal')
mylabel.pack(side=TOP)

entrylabel1 = Label(root, text="message to send",
                    font=20, bg='orange', fg='white')
entrylabel1.pack(side=TOP)

entry1 = Entry(root, width=40)
entry1.focus_set()
entry1.pack()

entrylabel2 = Label(root, text="auth-token",font=20, bg='orange', fg='white')
entrylabel2.pack()

entry2 = Entry(root, width=40)
entry2.focus_set()
entry2.pack()

def ping():
 y = entry2.get()
 x = entry1.get()
 payload = {
     'content': x
 }
 header = {
     'authorization': y
 }
 r = requests.post(
     'https://discord.com/api/v9/channels/1006913004576714883/messages', data=payload, headers=header)
 return x
 return r

button = Button(root, text='Start', width=25, fg='green')
button.configure(command=ping)
button.pack(side=RIGHT)

button1 = Button(root, text='Stop', width=25, command=root.destroy, fg='red')
button1.pack(side=LEFT)



root.mainloop()


