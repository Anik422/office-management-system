from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from MyDB import Mydatabase


class search_win:
    def __init__(self, root):
        global db
        db = Mydatabase()
        self.root = root
        self.root.title("Debit Data")
        self.root.geometry("1135x500+232+213")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))

        #   ========================  Title  ========================

        debit_lbl_title = Label(self.root, text="ADD DEBIT DATA DETAILS", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove").place(x=0 , y=0, width=1135, height=40 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((80, 40))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove").place(x=0, y=0, width=80, height=40)

         #   ========================  Title  ========================

        debit_lbl_title = Label(self.root, text="SEARCH DATA & CREATE PDF FILE", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove").place(x=0 , y=0, width=1135, height=40 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((80, 40))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove").place(x=0, y=0, width=80, height=40)

        #   ========================  search entry frame ========================

        search_entry_frame = Frame(self.root, bd=2, relief="groove", padx=2, bg="#b3cde0")
        search_entry_frame.place(x=195, y=45, width=750, height=40)




        #   ========================  search system ========================
        lbl_search = Label(search_entry_frame, text="Search By :", bg="#005b96", font=("times new roman",15, "bold"), fg="#ffffff")
        lbl_search.grid(row=0, column=0, padx=3)

         
        search_table_names = ['Dailay Account',
                            'Cash Receiv/Pay', 
                            'Managing Director',
                            'Stationary', 
                            'Office Maintenance', 
                            'Dailay Expendeture', 
                            'Convance', 
                            'TNT/Mobile Bill Office', 
                            'Courier', 
                            'Gift', 
                            'MD Houae', 
                            'MD Houae Baribadh', 
                            'MD Car', 
                            'MD Mobil & BKash', 
                            'MD Credit Card Payment', 
                            'Fees & Tex', 
                            'C & F', 
                            'Carring Cost', 
                            'Bill', 
                            'RENT SEVER OFFICE', 
                            'RENT HEAD OFFICE', 
                            'Renewal Fees', 
                            'Tannery Machinaries setup and Maintenance',
                            ]
        self.combobox_search_table_name = ttk.Combobox(search_entry_frame, values=search_table_names, font=("times new roman",12, "bold"), state='readonly')
        self.combobox_search_table_name.grid(row=0, column=1,padx=3)
        self.combobox_search_table_name.set("Select Table")
       

        self.search_date = DateEntry(search_entry_frame,state="readonly",selectmode='day',font=("times new roman",12, "bold") ,date_pattern="yyyy-mm-dd")
        self.search_date.grid(row=0, column=2, padx=3)

        lbl_search = Label(search_entry_frame, text="TO", bg="#005b96", font=("times new roman",12, "bold"), fg="#ffffff")
        lbl_search.grid(row=0, column=3, padx=3)

        self.search_to_date = DateEntry(search_entry_frame,state="readonly",selectmode='day', font=("times new roman",12, "bold") ,date_pattern="yyyy-mm-dd")
        self.search_to_date.grid(row=0, column=4, padx=3)

        #   ========================  search buttons ========================

        search_btn = Button(search_entry_frame, text="Search", bg="#00b159", font=("times new roman",12, "bold"), fg="#ffffff", width=7, command=self.date_to_date)
        search_btn.grid(row=0, column=5, padx=3)
        
        all_search_btn = Button(search_entry_frame, text="Show All", bg="#00b159", font=("times new roman",12, "bold"), fg="#ffffff", command=self.show_all)
        all_search_btn.grid(row=0, column=6, padx=3)


     #   ========================  table frame function ========================
    def col_3_table(self, t_name, date, cd):
        #   ========================  table lable frame ========================

        table_frame = LabelFrame(self.root, text=t_name+" Table View"+"({})".format(date), bd=2, relief="groove", font=("times new roman",20,"bold"), padx=2)
        table_frame.place(x=5, y=84, width=1125, height=405)


        #   ========================  show data table ========================
        
        show_data_frame = Frame(table_frame, bd=2, relief="groove")
        show_data_frame.place(x=0, y=5, width=1115, height=357)

        scroll_x = ttk.Scrollbar(show_data_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_data_frame, orient=VERTICAL)

        
        scroll_x.pack(side=BOTTOM, fill=X)
        self.data_3_deatlis = ttk.Treeview(show_data_frame, columns=("date", "description", "amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_y.config(command=self.data_3_deatlis.yview)

        scroll_x.config(command=self.data_3_deatlis.xview)
        self.data_3_deatlis.heading("date", text="Date")
        self.data_3_deatlis.heading("description", text="Description")
        if cd == 'C':
            self.data_3_deatlis.heading("amount", text="Ricived")
        elif cd == 'D':
            self.data_3_deatlis.heading("amount", text="Cost")
        self.data_3_deatlis["show"]="headings"


        self.data_3_deatlis.column('date', width=10)
        self.data_3_deatlis.column('description', width=700)
        self.data_3_deatlis.column('amount', width=10)

        self.data_3_deatlis.pack(fill=BOTH, expand=1)



     #   ========================  table frame function ========================self.
    def col_4_table(self, t_name, date):
        #   ========================  table lable frame ========================

        table_frame = LabelFrame(self.root, text=t_name+" Table View"+"({})".format(date), bd=2, relief="groove", font=("times new roman",20,"bold"), padx=2)
        table_frame.place(x=5, y=84, width=1125, height=405)


        #   ========================  show data table ========================
        
        show_data_frame = Frame(table_frame, bd=2, relief="groove")
        show_data_frame.place(x=0, y=5, width=1115, height=357)

        scroll_x = ttk.Scrollbar(show_data_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_data_frame, orient=VERTICAL)

        self.data_4_deatlis = ttk.Treeview(show_data_frame, columns=("date", "description", "ricived", "cost"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.data_4_deatlis.xview)
        scroll_y.config(command=self.data_4_deatlis.yview)

        self.data_4_deatlis.heading("date", text="Date")
        self.data_4_deatlis.heading("description", text="Description")
        self.data_4_deatlis.heading("ricived", text="Ricived")
        self.data_4_deatlis.heading("cost", text="Cost")
        self.data_4_deatlis["show"]="headings"


        self.data_4_deatlis.column('date', width=10)
        self.data_4_deatlis.column('description', width=500)
        self.data_4_deatlis.column('ricived', width=10)
        self.data_4_deatlis.column('cost', width=10)

        self.data_4_deatlis.pack(fill=BOTH, expand=1)



    #  # #   ========================  btn date to date search function ========================

    def date_to_date(self):
        table_name = self.combobox_search_table_name.get()
        date = self.search_date.get_date()
        toDate = self.search_to_date.get_date()
        if table_name == "Select Table":
             messagebox.showerror("Error", "Table name fields are requaired", parent=self.root)
        elif table_name == 'Cash Receiv/Pay' or table_name == 'Dailay Account':
            self.search_datToDate_data_view(table_name, date, toDate, "CD")
        elif table_name == 'Managing Director':
            self.search_datToDate_data_view(table_name, date, toDate, "C")
        else:
            self.search_datToDate_data_view(table_name, date, toDate, "D")

        


     # #   ========================  search date To date data  view ========================
    def search_datToDate_data_view(self, table_name, date, toDate, crdr):
        table_value = db.search_dateToDate_data_fetch(table_name, date, toDate, crdr)
        if len(table_value) == 0:
            messagebox.showerror("Error", "Table data nai", parent=self.root)
        else:
            try:
                if crdr == "CD":
                    self.col_4_table(table_name, str(date)+" To "+ str(toDate))
                    if len(table_value) != 0:
                        self.data_4_deatlis.delete(*self.data_4_deatlis.get_children())
                        for i in table_value:
                            self.data_4_deatlis.insert("", END, values=i)
                elif crdr == 'C':
                    self.col_3_table(table_name, "All Data", crdr)
                    if len(table_value) != 0:
                        self.data_3_deatlis.delete(*self.data_3_deatlis.get_children())
                        for i in table_value:
                            self.data_3_deatlis.insert("", END, values=i)
                else:
                    self.col_3_table(table_name, "All Data", crdr)
                    if len(table_value) != 0:
                        self.data_3_deatlis.delete(*self.data_3_deatlis.get_children())
                        for i in table_value:
                            self.data_3_deatlis.insert("", END, values=i)
            except Exception as exc:
                messagebox.showerror("Error", f"Some thing went wrong:{str(exc)}", parent=self.root)


    #  # #   ========================  btn show all function ========================
    def show_all(self):
        table_name = self.combobox_search_table_name.get()
        if table_name == "Select Table":
             messagebox.showerror("Error", "Table name fields are requaired", parent=self.root)
        elif table_name == 'Cash Receiv/Pay' or table_name == 'Dailay Account':
            self.search_table_all_data_view(table_name, "CD")
        elif table_name == 'Managing Director':
            self.search_table_all_data_view(table_name, "C")
        else:
            self.search_table_all_data_view(table_name, "D")


     # #   ========================  search table all data  view ========================
    def search_table_all_data_view(self, table_name, crdr):
        table_value = db.search_table_data_fetch(table_name, crdr)
        if len(table_value) == 0:
            messagebox.showerror("Error", "Table data nai", parent=self.root)
        else:
            try:
                if crdr == "CD":
                    self.col_4_table(table_name, "All Data")
                    if len(table_value) != 0:
                        self.data_4_deatlis.delete(*self.data_4_deatlis.get_children())
                        for i in table_value:
                            self.data_4_deatlis.insert("", END, values=i)
                elif crdr == 'C':
                    self.col_3_table(table_name, "All Data", crdr)
                    if len(table_value) != 0:
                        self.data_3_deatlis.delete(*self.data_3_deatlis.get_children())
                        for i in table_value:
                            self.data_3_deatlis.insert("", END, values=i)
                else:
                    self.col_3_table(table_name, "All Data", crdr)
                    if len(table_value) != 0:
                        self.data_3_deatlis.delete(*self.data_3_deatlis.get_children())
                        for i in table_value:
                            self.data_3_deatlis.insert("", END, values=i)
            except Exception as exc:
                messagebox.showerror("Error", f"Some thing went wrong:{str(exc)}", parent=self.root)




# select  *
# from `dailay account`
# where `date` >= '2022-05-15' and `date` <= '2022-05-16';


if __name__ == "__main__":
    root = Tk()
    obj = search_win(root)
    # obj.col_4_table()
    root.mainloop()