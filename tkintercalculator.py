from tkinter import *
cal = Tk()
v = StringVar()
def evaluate1(e):

    try:
        val= tEntry.get()
        tEntry.delete(0,END)
        tEntry.insert(END,eval(val))
    except SyntaxError as e:
        tEntry.insert(END,"Invalid!")
        print (e)
    except TypeError as t:
        tEntry.insert(END,"TE!")
        print (t)
    
def createButton(name,T,X,Y,F =("Times New Roman", 10, 'bold')):
    name = Button(cal, text = T,padx = 8, pady = 5, bd =8, fg = 'black',bg='powder blue',font = F)
    if T == "D":
        name.config(command=lambda :tEntry.delete(0, END))   
    elif T=="=":
        name.bind("<Button>",evaluate1 )
    else:
        name.bind("<Button>", lambda e : tEntry.insert(END,name['text']))
    # name.bind("<Key-=>",evaluate1)
    name.place(x=X,y=Y)
        
cal.title("Calculator")
cal.geometry('200x300')
cal.config(bg="Honeydew")
cal.resizable(0,0)

#Main Entry 
tEntry = Entry(cal,width = 18,textvariable =v,justify = 'right',text="", bg = 'powder blue',bd = 10, insertwidth = 1)
tEntry.config(font = (("Times New Roman", 15, 'bold')))
# tEntry.bind("<Key-=>",evaluate1)
tEntry.place(x=1, y=1)

#attach some fuctionality with tkinter window
cal.bind("<Key-=>",evaluate1)
cal.bind("<BackSpace>", lambda e :tEntry.delete(len(tEntry.get())-1))

#create buttons       
createButton("bt1","%",0,50)
createButton("bt2","(",60,50)
createButton("bt3",")",110,50)
createButton("bt4","+",160,50)
createButton("bt5","7",0,100)
createButton("bt6", "8",60,100)
createButton("bt7","9",110,100)
createButton("bt8","-",160,100)
createButton("bt9", "4", 0, 150)
createButton("bt10","5",60,150)
createButton("bt11","6",110,150)
createButton("bt12","*",160,150)
createButton("bt13","1",0,200)
createButton("bt14", "2",60,200)
createButton("bt15", "3",110,200)
createButton("bt16","/",160,200)
createButton("bt17",".",0,250)
createButton("bt18", "0",60,250)
createButton("bt19","D",110,250)
createButton("bt20","=",160,250)

cal.mainloop()

# l = ["","%","(",")","+","7","8","9","-","4","5","6","*","1","2","3","/",".","0","D","="]
# for i in range(1,21):
#     if i in (1,5,9,13,17):
#         createButton(f"bt{i}",l[i],0,50)