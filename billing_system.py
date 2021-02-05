import random
from tkinter import *


class FarmersApp:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Farmer's Market")

        title = Label(self.root, text="Farmer's Market", bd=12, relief=RIDGE, font=("Arial Black", 20), 
                      bg="#008000", fg="white").pack(fill=X)

        # ===================================variables===================================
        self.chai = IntVar()
        self.apples = IntVar()
        self.coffee = IntVar()
        self.milk = IntVar()
        self.oatmeal = IntVar()

        self.total_veggies = StringVar()

        self.c_name = StringVar()
        self.bill_no = StringVar()

        bill_num = random.randint(1000, 9999)

        self.bill_no.set(str(bill_num))
        self.phone = StringVar()

        # ======================================customer details label frame=================================
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=0, padx=15)
        
        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)
        
        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=2, padx=10)
        
        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)
        
        bill_name = Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=4, padx=10)
        
        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        # =======================================Items label frame==================================================
        veggies = LabelFrame(self.root, text="Items", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=GROOVE, bd=10)
        veggies.place(x=200, y=170, height=380, width=325)

        item1 = Label(veggies, text="Chai(3.11)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0, pady=11)
        item1_entry = Entry(veggies, borderwidth=2, width=15, textvariable=self.chai).grid(row=0, column=1, padx=10)

        item2 = Label(veggies, text="Apples(6)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0, pady=11)
        item2_entry = Entry(veggies, borderwidth=2, width=15, textvariable=self.apples).grid(row=1, column=1, padx=10)

        item3 = Label(veggies, text="Coffee(11.23)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0, pady=11)
        item3_entry = Entry(veggies, borderwidth=2, width=15, textvariable=self.coffee).grid(row=2, column=1, padx=10)

        item4 = Label(veggies, text="Milk(4.75)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3, column=0, pady=11)
        item4_entry = Entry(veggies, borderwidth=2, width=15, textvariable=self.milk).grid(row=3, column=1, padx=10)

        item5 = Label(veggies, text="Oatmeal(3.67)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0, pady=11)
        item5_entry = Entry(veggies, borderwidth=2, width=15, textvariable=self.oatmeal).grid(row=4, column=1, padx=10)

        # =======================================Total Bill===================================================
        total_bill = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        total_bill.place(x=800, y=170, width=330, height=372)

        bill_title = Label(total_bill, text="Total Bill", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3", fg="#6C3483").pack(fill=X)

        scrol_y = Scrollbar(total_bill, orient=VERTICAL)
        self.txtarea = Text(total_bill, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =============================================Billing menu=================================================
        billing_menu = LabelFrame(self.root, text="Billing Summery", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_veggies = Label(billing_menu, text="Total Items Price", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=0, column=0)
        total_veggies_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_veggies).grid(row=0, column=1, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=lambda: self.total()).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", command=lambda: self.clear()).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483", width=8, command=lambda: self.exit1()).grid(row=0, column=2, padx=10, pady=6)
        self.intro()

    def intro(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\tWELCOME TO FARMER's MARKET\n\tPhone-No.7709162640")
        self.txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END, "\n====================================\n")
        self.txtarea.insert(END, "\nItems\t\tQty\tPrice\n")
        self.txtarea.insert(END, "\n====================================\n")

    def total(self):
        try:
            self.ch = self.chai.get() * 3.11
            if self.chai.get() > 0 and self.milk.get() > 0:
                self.milk.set((self.milk.get()) - 1)
        except:
            self.chai.set(0)
            self.ch = 0

        try:
            if self.apples.get() >= 3:
                self.ap = self.apples.get() * 4.50
            else:
                self.ap = self.apples.get() * 6.00
        except:
            self.apples.set(0)
            self.ap = 0

        try:
            self.cf = ((self.coffee.get() // 2) + (self.coffee.get() % 2)) * 11.23
        except:
            self.coffee.set(0)
            self.cf = 0

        try:
            self.mk = self.milk.get() * 4.75
        except:
            self.milk.set(0)
            self.mk = 0

        try:
            self.om = self.oatmeal.get() * 3.69
        except:
            self.oatmeal.set(0)
            self.om = 0

        total_veggies_price = (self.ch + self.ap + self.cf + self.mk + self.om)
        self.total_veggies.set(f"$ {total_veggies_price}")

        self.total_all_bill = round(total_veggies_price, 2)
        self.total_all_bil = f"$ {self.total_all_bill}"
        self.total_bill()

    def total_bill(self):
        self.intro()
        if self.chai.get() != 0:
            self.txtarea.insert(END, f"Chai\t\t {self.chai.get()}\t{self.ch}\n")
        if self.apples.get() != 0:
            self.txtarea.insert(END, f"Apples\t\t {self.apples.get()}\t{self.ap}\n")
        if self.coffee.get() != 0:
            self.txtarea.insert(END, f"Coffee\t\t {self.coffee.get()}\t{self.cf}\n")
        if self.milk.get() != 0:
            self.txtarea.insert(END, f"Milk\t\t {self.milk.get()}\t{self.mk}\n")
        if self.oatmeal.get() != 0:
            self.txtarea.insert(END, f"Oatmeal\t\t {self.oatmeal.get()}\t{self.om}\n")

        self.txtarea.insert(END, f"------------------------------------\n")

        self.txtarea.insert(END, f"Total Bill Amount : {self.total_all_bil}\n")
        self.txtarea.insert(END, f"------------------------------------\n")

    def clear(self):
        self.txtarea.delete(1.0, END)
        self.chai.set(0)
        self.apples.set(0)
        self.coffee.set(0)
        self.milk.set(0)
        self.oatmeal.set(0)
        self.total_veggies.set(0)

        self.c_name.set('')
        self.phone.set('')
        self.bill_no.set(str(random.randint(1000, 9999)))

    def exit1(self):
        self.root.destroy()


basket = Tk()
obj = FarmersApp(basket)
basket.mainloop()
