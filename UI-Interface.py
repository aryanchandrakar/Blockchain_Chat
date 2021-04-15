from tkinter import *
import restnode
master = Tk()
# VARS
message = StringVar()
myAddr = StringVar()
peerHost = StringVar()
peerPort = IntVar()
# CALLBACKS
def send():
    print("Send message")
    me.add_data(message.get())
    message.set("")
def peer():
    print("Peer with node")
    me.peer(peerHost.get(), peerPort.get())
    peerHost.set("")
    peerPort.set("")
# UI ELEMENTS
messagesBlock = Text(master)
messageBox = Entry(master, textvariable=message)
sendBtn = Button(master, text="Send", command=send)
statusLabel = Label(master, textvariable=myAddr)
pipLabel = Label(master, text="Host IP:")
hostBox = Entry(master, textvariable=peerHost)
ppLabel = Label(master, text="Port")
portBox = Entry(master, textvariable=peerPort)
peerBtn = Button(master, text="Peer", command=peer)
ccLabel = Label(master, text="")
# UI GRIDDING
messagesBlock.grid(row=0, column=0, columnspan=2, rowspan=6)
messageBox.grid(row=6, column=0)
sendBtn.grid(row=6, column=1)
statusLabel.grid(row=0, column=2)
pipLabel.grid(row=1, column=2)
hostBox.grid(row=2, column=2)
ppLabel.grid(row=3, column=2)
portBox.grid(row=4, column=2)
peerBtn.grid(row=5, column=2)
ccLabel.grid(row=6, column=2)
host = restnode.ip()
port = restnode.getPort()
myAddr.set("Peer: ({host}, {port})".format(host=host, port=port))
me = restnode.start(port)
def updateChatbox():
    data = ""
    for block in me.chain.blocks:
        data += "\n".join(block.data)+"\n"
    print(data)
    messagesBlock.delete('1.0', END)
    messagesBlock.insert('1.0', data)
    master.after(100, updateChatbox)
master.after(100, updateChatbox)
master.mainloop()
