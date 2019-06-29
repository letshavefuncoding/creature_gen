#This is just a very simple GUI for to add button fuctionality 
#and to display the output of generator.

from tkinter import *
from files import generator as gen

output=""

#Take in event, clear the display, and add new info to the display.
def postframe( event, product ):
    product.delete("1.0",END)
    output=gen.main()
    for item in output:
        f=item+"\n"
        product.insert(END,f)
    return 0






base= Tk()#
base.title("Monster gen")
base.geometry('350x200')



base.wm_iconbitmap('dist/main/files/images/swag_Oda_icon.ico')
product=Text(base,bg="grey")


Button=Button(base,text="generate monstrosity")
Button.bind("<Button-1>",lambda event :postframe(event,product))
Button.grid(column=0, columnspan=1,sticky=N)
product.grid(row=0,column=2,columnspan=1,padx=5, ipadx=2,ipady=1)
base.mainloop()