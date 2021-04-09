import tkinter
from datetime import datetime
counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 66600:
                display = "starting.."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
                display: str
            label['text']=display
            label.after(1000, count)
            counter += 1
    count()
def start(label):
    global running
    running=True
    counter_label(label)
    s['state'] = 'disabled'
    st['state'] = 'normal'
    res['state'] = 'normal'
def stop():
    global running
    s['state']='normal'
    st['state']='disabled'
    res['state']='normal'
    running=False
def reset(label):
    global counter
    counter = 66600
    if running == False:
        res['state']='disabled'
        label['text']='welcome!'
    else:
        label['text']='starting..'

root=tkinter.Tk()
root.title("StopWatch")
root.minsize(width=250,height=70)
label = tkinter.Label(root,text="welcome!",fg="black",font="verdana 30 bold")
label.pack()
f=tkinter.Frame(root)
s=tkinter.Button(f,text='start',width=6,command=lambda:start(label))
st=tkinter.Button(f,text='stop',width=6,state='disabled',command=stop)
res=tkinter.Button(f,text='reset',width=6,state='disabled',command=lambda:reset(label))
f.pack(anchor = 'center')
s.pack(side="left")
st.pack(side="left")
res.pack(side="left")
root.mainloop()