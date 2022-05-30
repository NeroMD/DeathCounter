import pynput.keyboard  
from tkinter import *
import threading

reader = ''
with open('count.txt','r') as fileRead:
    reader = fileRead.read()


deathCount = int(reader)


def window():
    root = Tk()
    myLabel=Label(root,text='DeathCount: {}'.format(deathCount))
    myLabel.pack()
    def refresher():

        myLabel.configure(text='DeathCount: {}'.format(deathCount))
        root.after(1000, refresher)
    refresher()
    root.mainloop()




def increaseCount():
    with open('count.txt','w') as fileWrite:
        fileWrite.write(str(deathCount))

def listen(key):
    global deathCount
    a=str(key)
    print(a)
    if a == "'q'":
        deathCount+=1

        increaseCount()



thread = threading.Thread(target=window)


listener = pynput.keyboard.Listener(on_press=listen)

with listener:
    thread.start()
    listener.join()




