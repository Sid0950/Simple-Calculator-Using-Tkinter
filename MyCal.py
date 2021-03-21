#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox


# In[13]:


class MyCal:
    
    def __init__(self,root):
        self.root = root
        self.root.title("My App")
        self.root.geometry("600x400+0+0")
        
        
        #Make Frames
        frame1 = Frame(self.root)
        frame1.grid()
        
        frame2 = Frame(frame1, width = 600, height = 200, relief=RIDGE, bd = 10)
        frame2.grid(row=0, column=0)
        
        frame3 = Frame(frame1, width = 600, height = 200, relief=RIDGE, bd = 10)
        frame3.grid(row=1, column=0)
        
        #==================================================================================#
        
        #Define variables type which will take values from the user
        BasePrice = IntVar()
        Profit = IntVar()
        SellingPrice = IntVar()
        
        
        #Make a Variable lable for the Base Price
        self.BasePrice_label = Label(frame2, text="Base Price($)",font =('arial',14,'bold'), bd=12)
        #Label Position
        self.BasePrice_label.grid(row=0, column=0)
        
        #Make a Variable to fetch the Base Price from the user
        self.BasePrice_var = Entry(frame2, textvariable = BasePrice,font =('arial',14,'bold'), bd=12)
        #Position of the Entry Box
        self.BasePrice_var.grid(row=0, column=1)
        
        #==================================================================================#
        
        
        #Make a Variable lable for the Profit
        self.Profit_label = Label(frame2, text="Profit(%)",font =('arial',14,'bold'), bd=12)
        #Label Position
        self.Profit_label.grid(row=1, column=0)
        
        #Make a Variable to fetch the Profit from the user
        self.Profit_var = ttk.Combobox(frame2, textvariable = Profit, font =('arial',14,'bold'))
        self.Profit_var['value']=(0,5,10,15,20,25,30,35,40,45,50)
        self.Profit_var.current(0)
        #Position of the Entry Box
        self.Profit_var.grid(row=1, column=1)
        
        #==================================================================================#
        
        #Make a Variable lable for the Selling Price
        self.SellingPrice_label = Label(frame2, text="Selling Price($)",font =('arial',14,'bold'), bd=12)
        #Label Position
        self.SellingPrice_label.grid(row=2, column=0)
        
        #Make a Variable to display the resulting Selling Price from the user
        self.SellingPrice_var = Entry(frame2, textvariable = SellingPrice,font =('arial',14,'bold'), bd=12)
        #Position of the Displace Box
        self.SellingPrice_var.grid(row=2, column=1)
        
        #====================================Calculations==================================================#
        def Cal_Func():
            
            bp = float(BasePrice.get())
            pr = float(Profit.get())
            sp = bp + (bp*pr)/100
            SellingPrice.set(sp) 
            
        #===============================Resets all the Values to Null=====================================#
            
        def Reset():
            BasePrice.set("")
            Profit.set("")
            SellingPrice.set("")
            
        def Exit():
            root.destroy()
            
            
        
        #================================================Commands Buttons==============================================#
        
        #Create Buttons for the result which is Selling Price, for resetting and exiting the app
        self.SellingPrice_bt = Button(frame3, text="Calculate", command = Cal_Func,font =('arial',14,'bold'), bd=12,pady=12,padx=4).grid(row=0,column=0)
        self.Reset_bt = Button(frame3, text="Reset", command=Reset,font =('arial',14,'bold'), bd=12,pady=12,padx=4).grid(row=0,column=1)
        self.Exit_bt = Button(frame3, text="Exit", command = Exit,font =('arial',14,'bold'), bd=12,pady=12,padx=4).grid(row=0,column=2)
        
 
        
if __name__ == '__main__':
    root= Tk()
    application = MyCal(root)
    root.mainloop()
    



# In[ ]:




