#simple calc
from tkinter import *
top = Tk()
top.title("simple calc")
top.maxsize(300,495)
e = Entry(top,width = 35 , borderwidth = 5 , bg = "white",fg = "#b71c1c")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    #e.delete()
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
      e.insert(0,f_num + int(second_number))

    if math == "subtraction":
      e.insert(0,f_num - int(second_number))

    if math == "multiplication":
      e.insert(0,f_num * int(second_number))

    if math == "division":
      e.insert(0,f_num / int(second_number))





def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

    

#define buttons
button_1=Button(top,text ="1",padx=40,pady=20,command=lambda : button_click(1),fg = "white",bg="#b71c1c")
button_2=Button(top,text ="2",padx=40,pady=20,command=lambda : button_click(2),fg = "white",bg="#b71c1c")
button_3=Button(top,text ="3",padx=40,pady=20,command=lambda : button_click(3),fg = "white",bg="#b71c1c")
button_4=Button(top,text ="4",padx=40,pady=20,command=lambda : button_click(4),fg = "white",bg="#b71c1c")
button_5=Button(top,text ="5",padx=40,pady=20,command=lambda : button_click(5),fg = "white",bg="#b71c1c")
button_6=Button(top,text ="6",padx=40,pady=20,command=lambda : button_click(6),fg = "white",bg="#b71c1c")
button_7=Button(top,text ="7",padx=40,pady=20,command=lambda : button_click(7),fg = "white",bg="#b71c1c")
button_8=Button(top,text ="8",padx=40,pady=20,command=lambda : button_click(8),fg = "white",bg="#b71c1c")
button_9=Button(top,text ="9",padx=40,pady=20,command=lambda : button_click(9),fg = "white",bg="#b71c1c")
button_0=Button(top,text ="0",padx=40,pady=20,command=lambda : button_click(0),fg = "white",bg="#b71c1c")
button_add=Button(top,text ="+",padx=39,pady=20,command= button_add,fg  = "#b71c1c",bg = "white")
button_subtract=Button(top,text ="-",padx=41,pady=20,command= button_subtract,fg = "#b71c1c",bg = "white")
button_multiply=Button(top,text ="*",padx=40,pady=20,command= button_multiply,fg  = "#b71c1c",bg = "white")
button_divide=Button(top,text ="/",padx=42,pady=20,command= button_divide,fg  = "#b71c1c",bg = "white")
button_equal=Button(top,text ="=",padx=90,pady=20,command=button_equal,fg  = "#b71c1c",bg = "white")
button_clear=Button(top,text ="Clear",padx=79,pady=20,command=button_clear,fg  = "red",bg = "white")


#put buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan = 2)
button_equal.grid(row=5,column=1,columnspan = 2)

button_subtract.grid(row = 6,column = 0)
button_multiply.grid(row = 6,column = 1)
button_divide.grid(row = 6,column = 2)

def openQ():
  
  quad = Tk()
  quad.title("Quadratic equations solver")

  #frame to hold the entry widegts for digits input
  frames = LabelFrame(quad,text="enter values",padx = 50,pady =50)
  frames.pack(padx = 10 ,pady =  10)
  #entry for first digit
  first_n = Entry(frames,width = 35,borderwidth = 5,fg = "gold",bg="darkblue")
  first_n.pack()
  #entry for second digit
  second_n = Entry(frames,width = 35,borderwidth = 5,fg = "gold",bg="darkblue")
  second_n.pack()
  #entry for third digit
  third_n = Entry(frames,width = 35,borderwidth = 5,fg = "gold",bg="darkblue")
  third_n.pack()

  # frame to hold the answers
  frames2 = LabelFrame(quad,text = "Answers",padx = 100 ,pady = 100 ,borderwidth =  5,fg = "gold",bg  = "darkblue")
  frames2.pack(padx =  10 , pady = 10)

  
 # to show the user which of the entries are to be put 
  first_n.insert(0,"b")
  second_n.insert(0,"a")
  third_n.insert(0,"c")

  # frame to hold the answers
  frames2 = LabelFrame(quad,text = "Answers",padx = 100 ,pady = 100 ,borderwidth =  5,fg = "gold",bg  = "darkblue")
  frames2.pack(padx =  10 , pady = 10)



  def Quad():
    eqn =  str(second_n.get()+"x2 - "+first_n.get()+"x - "+third_n.get())
    eqn = str(eqn)
    eqn2 = Label(frames2,text =eqn,bg = "darkblue",fg = "gold")
    eqn2.pack()

    import math as m
    
    # to get the digits from the entry
    b = first_n.get()
    a = second_n.get()
    c = third_n.get()
  #stating variables to make he calculation easier
    b=int(b)
    a=int(a)
    c=int(c)
  # to show that the anser is coming 
    answer = Label(frames2,text = "The answer is :",bg = "darkblue",fg = "gold")
    answer.pack()
  #the actual calculation
    x= -b
    x1 =  m.sqrt(b*b - (4*a*c))
    x2 = (x+x1)/(2 * a)
    x3 = (x-x1)/(2 * a)
  #showing tghe answer
    answer2 = Label(frames2,text = x2, bg = "darkblue",fg = "gold")
    answer2.pack()

    answer3= Label(frames2,text = x3, bg = "darkblue",fg = "gold")
    answer3.pack()



    print("The answer is ")
    
    print(x2,"\n")

    print(x3)
  #button to start calculation
  button_quad=Button(frames,text="Q",padx = 40,pady = 20,command = Quad ,fg = "red",bg ="white")
  button_quad.pack()


  quad.mainloop()



button_open = Button(top,text = "openQ",padx = 50,pady = 10,bg = "white",fg = "red",command = openQ)
button_open.grid(row = 7,column = 0,columnspan = 4)
top.mainloop()







