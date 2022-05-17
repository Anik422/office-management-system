from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry #pip install tkcalender
from PIL import Image, ImageTk
from MyDB import Mydatabase


class Debit_win:
    def __init__(self, root):
        global db
        db = Mydatabase()
        self.root = root
        self.root.title("Debit Data")
        self.root.geometry("1210x500+155+213")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))

        #   ========================  Title  ========================

        debit_lbl_title = Label(self.root, text="ADD DEBIT DATA DETAILS", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove")
        debit_lbl_title.place(x=0 , y=0, width=1210, height=40 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((80, 40))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove")
        logoLblImg.place(x=0, y=0, width=80, height=40)

         #   ========================  Title  ========================

        debit_lbl_title = Label(self.root, text="ADD DEBIT DATA DETAILS", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove")
        debit_lbl_title.place(x=0 , y=0, width=1210, height=40 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((80, 40))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove").place(x=0, y=0, width=80, height=40)

   #   ========================  variables  ========================
        self.description = StringVar()
        self.table_name = StringVar()
        self.amount = IntVar()



        #   ========================  label_frame left ========================

        lable_frame_laft = LabelFrame(self.root, text="Debit Detatls", bd=2, relief="groove", font=("times new roman",20,"bold"), padx=2)
        lable_frame_laft.place(x=5, y=70, width=425, height=405)
         #   ========================  Date label nad entry ========================
        global entry_date
        lbl_date = Label(lable_frame_laft, justify=LEFT, anchor="w", text="Date : ", font=("times new roman",15,"bold"), padx=2, pady=6)
        lbl_date.grid(row=0, column=0)
        entry_date = DateEntry(lable_frame_laft,state="readonly",selectmode='day', font=("times new roman",15) ,date_pattern="yyyy-mm-dd")
        entry_date.grid(row=0, column=1, padx=10, pady=10, ipadx=63)
 
        # #   ========================  Description label nad entry ========================
        table_names = ['Cash Receiv/Pay', 
                        'Stationary', 
                        'Office Maintenance', 
                        'Dailay Expendeture', 
                        'Convance', 
                        'TNT/Mobile Bill Office', 
                        'Courier', 'Gift', 'MD Houae', 
                        'MD Houae Baribadh', 'MD Car', 
                        'MD Mobil & BKash', 
                        'MD Credit Card Payment', 
                        'Managing Director', 
                        'Fees & Tex', 
                        'C & F', 
                        'Carring Cost', 
                        'Bill', 
                        'RENT SEVER OFFICE', 
                        'RENT HEAD OFFICE', 
                        'Renewal Fees', 
                        'Tannery Machinaries setup and Maintenance']
        lbl_table_name = Label(lable_frame_laft, justify=LEFT, anchor="w", text="Table : ", font=("times new roman",15,"bold"), padx=2, pady=6)
        lbl_table_name.grid(row=1, column=0)
        combobox_table_name = ttk.Combobox(lable_frame_laft, values=table_names, font=("times new roman",15), state='readonly', textvariable=self.table_name)
        combobox_table_name.grid(row=1, column=1, padx=10, pady=10, ipadx=20)
        combobox_table_name.set("Select table")
       
        #   ========================  cost Cash label nad entry ========================
        lbl_ricived_cash = Label(lable_frame_laft, justify=LEFT, anchor="w", text="Amount : ", font=("times new roman",15,"bold"), bg=None, padx=2, pady=6)
        lbl_ricived_cash.grid(row=2, column=0)
        spinbox_ricived_cash = ttk.Spinbox(lable_frame_laft, from_=0, to=100000000000, font=("times new roman",15), textvariable=self.amount)
        spinbox_ricived_cash.grid(row=2, column=1, padx=10, pady=10, ipadx=23)

        #   ========================  Description label nad entry ========================

        lbl_description = Label(lable_frame_laft, justify=LEFT, anchor="w", text="Description : ", font=("times new roman",15,"bold"), bg=None, padx=2, pady=6)
        lbl_description.grid(row=3, column=0)
        lbl_entry = ttk.Entry(lable_frame_laft, font=("times new roman",15), textvariable=self.description)
        lbl_entry.grid(row=3, column=1, padx=10, pady=10, ipadx=30)
        
        #   ========================  Button fream ========================
        btn_fream = Frame(lable_frame_laft, bd=2, relief="groove")
        btn_fream.place(x=10, y=250, width=400, height=45)

        #   ========================  Delete Button ========================
        delete_btn = Button(btn_fream, text="Delete", bg="#fe4a49", font=("times new roman",15), fg="#ffffff", width=6)
        delete_btn.grid(row=0, column=0, padx=5)
       
        #   ========================  update Button ========================
        update_btn = Button(btn_fream, text="Update", bg="#fed766", font=("times new roman",15), fg="#ffffff", width=6)
        update_btn.grid(row=0, column=1, padx=5)
      
        #   ========================  Reset Button ========================
        reser_btn = Button(btn_fream, text="Reset", bg="#2ab7ca", font=("times new roman",15), fg="#ffffff", width=7)
        reser_btn.grid(row=0, column=2, padx=5)
       
       
        #   ========================  Add Button ========================
        add_btn = Button(btn_fream, text="Add", bg="#00b159", font=("times new roman",15), fg="#ffffff", width=9, command=self.add_data)
        add_btn.grid(row=0, column=3, padx=5)



 #   ========================  search frame ========================
        search_frame = Frame(self.root, bd=2, relief="groove")
        search_frame.place(x=440, y=50, width=510, height=30)


        #   ========================  search system ========================
        lbl_search = Label(search_frame, text="Search By :", bg="#005b96", font=("times new roman",12, "bold"), fg="#ffffff")
        lbl_search.grid(row=0, column=0, padx=3)

         
        table_names.append("Dailay Account")
        self.combobox_search_table_name = ttk.Combobox(search_frame, values=table_names, font=("times new roman",10, "bold"), state='readonly')
        self.combobox_search_table_name.grid(row=0, column=1,padx=3)
        self.combobox_search_table_name.set("Select Table")
       

        self.search_date = DateEntry(search_frame,state="readonly",selectmode='day',font=("times new roman",10, "bold") ,date_pattern="yyyy-mm-dd")
        self.search_date.grid(row=0, column=2, padx=3)

        # lbl_search = Label(search_frame, text="TO", bg="#005b96", font=("times new roman",10, "bold"), fg="#ffffff")
        # lbl_search.grid(row=0, column=3, padx=3)

        # search_to_date = DateEntry(search_frame,state="readonly",selectmode='day', font=("times new roman",10, "bold") ,date_pattern="yyyy-mm-dd")
        # search_to_date.grid(row=0, column=4, padx=3)

        #   ========================  search buttons ========================

        search_btn = Button(search_frame, text="Search", bg="#00b159", font=("times new roman",10, "bold"), fg="#ffffff", width=7, command=self.search_table_view)
        search_btn.grid(row=0, column=3, padx=3)
        
        all_search_btn = Button(search_frame, text="Show All", bg="#00b159", font=("times new roman",10, "bold"), fg="#ffffff", command=self.search_table_all_data_view)
        all_search_btn.grid(row=0, column=4, padx=3)


        #   ========================  table frame function ========================
    def table_data(self, view_table_name, date):
        #   ========================  table lable frame ========================

        table_frame = LabelFrame(self.root, text= view_table_name + " Table View"+"({})".format(date), bd=2, relief="groove", font=("times new roman",20,"bold"), padx=2)
        table_frame.place(x=440, y=85, width=750, height=405)


        #   ========================  show data table ========================
        
        show_data_frame = Frame(table_frame, bd=2, relief="groove")
        show_data_frame.place(x=0, y=10, width=740, height=357)

        scroll_x = ttk.Scrollbar(show_data_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_data_frame, orient=VERTICAL)

        self.data_deatlis = ttk.Treeview(show_data_frame, columns=("date", "description", "amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.data_deatlis.xview)
        scroll_y.config(command=self.data_deatlis.yview)

        self.data_deatlis.heading("date", text="Date")
        self.data_deatlis.heading("description", text="Description")
        self.data_deatlis.heading("amount", text="Amount")
        self.data_deatlis["show"]="headings"


        self.data_deatlis.column('date', width=10)
        self.data_deatlis.column('description', width=300)
        self.data_deatlis.column('amount', width=30)

        self.data_deatlis.pack(fill=BOTH, expand=1)

        
    # #   ========================  add data ========================
    def add_data(self):
        if self.description.get() == "":
            messagebox.showerror("Error", "Description fields are requaired")
        elif self.amount.get() <= 0:
            messagebox.showerror("Error", "Amount fields are requaired")
        elif self.table_name.get() == "Select table":
            messagebox.showerror("Error", "Table name fields are requaired")
        else:
            try:
                dt = str(entry_date.get_date())
                des = self.description.get()
                t_name = self.table_name.get()
                amount = self.amount.get()
                db.table_data_entry(dt, des, amount, "D", t_name)
                self.table_data(t_name, dt)
                self.add_table_data_view(t_name)
                messagebox.showinfo("Success", "Successful  Data Add.", parent=self.root)
            except Exception as ex:
                print(ex)
                messagebox.showerror("Error", f"Some thing went wrong:{str(ex)}", parent=self.root)

    # #   ========================  add table data  view ========================
    def add_table_data_view(self, table_nmae):
        table_value = db.add_table_data_fetch(table_nmae, "D")
        if len(table_value) != 0:
            self.data_deatlis.delete(*self.data_deatlis.get_children())
            for i in table_value:
                self.data_deatlis.insert("", END, values=i)
    
    # #   ========================  search table data  view ========================
    def search_table_view(self):
        table_name = self.combobox_search_table_name.get()
        search_date = self.search_date.get_date()
        if table_name == "Select Table":
             messagebox.showerror("Error", "Table name fields are requaired", parent=self.root)
        else:
            table_value = db.search_table_fetch(table_name, "D", search_date)
            if len(table_value) == 0:
                messagebox.showerror("Error", "Table data nai", parent=self.root)
            else:
                try:
                    self.table_data(table_name, search_date)
                    if len(table_value) != 0:
                        self.data_deatlis.delete(*self.data_deatlis.get_children())
                        for i in table_value:
                            self.data_deatlis.insert("", END, values=i)
                except Exception as exc:
                    messagebox.showerror("Error", f"Some thing went wrong:{str(exc)}", parent=self.root)


    # #   ========================  search table all data  view ========================
    def search_table_all_data_view(self):
        table_name = self.combobox_search_table_name.get()
        if table_name == "Select Table":
             messagebox.showerror("Error", "Table name fields are requaired", parent=self.root)
        else:
            table_value = db.search_table_all_data_fetch(table_name, "D",)
            if len(table_value) == 0:
                messagebox.showerror("Error", "Table data nai", parent=self.root)
            else:
                try:
                    self.table_data(table_name, "All Data")
                    if len(table_value) != 0:
                        self.data_deatlis.delete(*self.data_deatlis.get_children())
                        for i in table_value:
                            self.data_deatlis.insert("", END, values=i)
                except Exception as exc:
                    messagebox.showerror("Error", f"Some thing went wrong:{str(exc)}", parent=self.root)











if __name__ == "__main__":
    root = Tk()
    obj = Debit_win(root)
    root.mainloop()