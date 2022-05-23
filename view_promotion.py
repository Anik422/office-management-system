from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry #pip install tkcalender
from PIL import Image, ImageTk
from MyDB import Mydatabase


class View_Promotion:
    def __init__(self, root):
        global db
        db = Mydatabase()
        self.root = root
        self.root.title("View & Promotion")
        self.root.geometry("1210x550+155+170")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))


        #   ========================  Title  ========================

        credit_lbl_title = Label(self.root, text="VIEW & PROMOTION", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove")
        credit_lbl_title.place(x=0 , y=0, width=1210, height=40 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((80, 40))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove")
        logoLblImg.place(x=0, y=0, width=80, height=40)


        #   ========================  body image ========================
        clear_frame = Frame(self.root)
        clear_frame.place(x=0, y=85, width=1210, height=475)
        body_img = Image.open("images/promotion.jpeg")
        body_img = body_img.resize((1210, 475))
        self.photoBodyImg = ImageTk.PhotoImage(body_img)
        bodyLblImg = Label(clear_frame, image=self.photoBodyImg, bd=4, relief="groove")
        bodyLblImg.place(x=0, y=0, width=1210, height=475)


        #   ========================  button frame Image  ========================
        btn_frame = Frame(self.root, bd=2, relief="groove")
        btn_frame.place(x=0, y=40, width=1210, height=45)
        #   ========================  button  Image  ========================
        advance_salary = Button(btn_frame, text="Employee Promotion", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.employee_promotion)
        advance_salary.grid(row=0, column=0, padx=5)


        add_emp = Button(btn_frame, text="See Employee", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.search_frame)
        add_emp.grid(row=0, column=1, padx=5)


        # advance_salary = Button(btn_frame, text="Advance Salary", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove")
        # advance_salary.grid(row=0, column=2, padx=5)
        

        # add_dep = Button(btn_frame, text="Due Salary", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove")
        # add_dep.grid(row=0, column=3, padx=5)

        # add_dep = Button(btn_frame, text="Add Department", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove")
        # add_dep.grid(row=0, column=4, padx=5)
    
    #   ========================  promotion variable  ========================
        self.employee_id = IntVar()
        self.new_emp_dep = StringVar()
        self.new_salary = IntVar()
    #   ========================  search variable  ========================
        self.search_emp_id = IntVar()


    #   ========================  employree promotion frame  ========================
    def employee_promotion(self):
        self.clear_func()
        pro_lbl_frame = LabelFrame(self.root, text="Promotion Employee", font=("times new roman",20,"bold"), bd=2, relief="groove")
        pro_lbl_frame.place(x=385, y=135, width=450, height=330)



        emp_id = db.fatch_employee_id()
        lbl_emp_id = Label(pro_lbl_frame, text="Employee ID :", font=("times new roman",15,"bold"))
        lbl_emp_id.grid(row=0, column=0, pady=20, padx=20)
        entry_emp_id = ttk.Combobox(pro_lbl_frame, values=emp_id, font=("times new roman",13, "bold"), state='readonly', textvariable=self.employee_id)
        entry_emp_id.set("Select ID")
        entry_emp_id.grid(row=0, column=1, pady=20, padx=5, ipadx=7, ipady=2)



        dep_name = db.fatch_department_name()
        lbl_dep = Label(pro_lbl_frame, text="Department :", font=("times new roman",15,"bold"))
        lbl_dep.grid(row=1, column=0, pady=5, padx=30)
        entry_dep = ttk.Combobox(pro_lbl_frame, values=dep_name, font=("times new roman",13, "bold"), state='readonly', textvariable=self.new_emp_dep)
        entry_dep.set("Select Department")
        entry_dep.grid(row=1, column=1, pady=20, padx=5, ipadx=7, ipady=2)


        lbl_emp_pro_amount = Label(pro_lbl_frame, text="New Salary :", font=("times new roman",15,"bold"))
        lbl_emp_pro_amount.grid(row=3, column=0, pady=5, padx=20)
        entry_emp_pro_amount = ttk.Spinbox(pro_lbl_frame, from_=0, to=99999999, font=("times new roman",15), textvariable=self.new_salary)
        entry_emp_pro_amount.grid(row=3, column=1, pady=5, padx=5)


        sub_btn_sel = Button(pro_lbl_frame, text="Promotion", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove", command=self.promotion_function)
        sub_btn_sel.place(x=330, y=230, width=80, height=40)


        sub_btn_sel = Button(pro_lbl_frame, text="Clear", font=("times new roman",15,"bold"), bg="#fe4a49", fg="#eeeeee", bd=2, relief="groove", command=lambda : self.employee_promotion())
        sub_btn_sel.place(x=230, y=230, width=80, height=40) 


    # ================================ promotion function=======================
    def promotion_function(self):
        emp_id = self.employee_id.get()
        new_dep = self.new_emp_dep.get()
        new_sel = self.new_salary.get()
        if emp_id == "Select ID":
            messagebox.showerror("Error", "Please, Select the employee id!", parent=self.root)
        elif new_dep == "Select Department":
            messagebox.showerror("Error", "Please, Select the Department!", parent=self.root)
        elif new_sel == 0:
            messagebox.showerror("Error", "Please, Provide the New Salary!", parent=self.root)
        else:
            try:
                db.employee_promotion(new_dep, new_sel, emp_id)
                messagebox.showinfo("Success", f"Successfully Update Imaployee.\nID : {emp_id}")
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)

    # ================================ see imployee=======================
    # ================================ search system=======================
    def search_frame(self):
        self.clear_func()
        #   ========================  search entry frame ========================

        search_entry_frame = Frame(self.root, bd=2, relief="groove", padx=2, bg="#b3cde0")
        search_entry_frame.place(x=372, y=90, width=465, height=40)


        #   ========================  search system ========================
        lbl_search = Label(search_entry_frame, text="Search By :", bg="#005b96", font=("times new roman",15, "bold"), fg="#ffffff")
        lbl_search.grid(row=0, column=0, padx=3)

         
        search_emp_Ids = db.fatch_employee_id()
        self.combobox_search_emp_Id = ttk.Combobox(search_entry_frame, values=search_emp_Ids, font=("times new roman",12, "bold"), state='readonly')
        self.combobox_search_emp_Id.grid(row=0, column=1,padx=3)
        self.combobox_search_emp_Id.set("Select ID")
       

        #   ========================  search buttons ========================

        search_btn = Button(search_entry_frame, text="Search", bg="#00b159", font=("times new roman",12, "bold"), fg="#ffffff", width=7, command=self.search_one_employee)
        search_btn.grid(row=0, column=2, padx=3)
        
        all_search_btn = Button(search_entry_frame, text="Show All", bg="#00b159", font=("times new roman",12, "bold"), fg="#ffffff", command=self.search_all_employee)
        all_search_btn.grid(row=0, column=3, padx=3)

    #   ========================  employee view table ========================
    def view_teble(self):
        table_frame = LabelFrame(self.root, text="View Employee", bd=2, relief="groove", font=("times new roman",20,"bold"), padx=2)
        table_frame.place(x=5, y=130, width=1200, height=430)


        #   ========================  show data table ========================
        
        show_data_frame = Frame(table_frame, bd=2, relief="groove")
        show_data_frame.place(x=0, y=5, width=1190, height=350)

        scroll_x = ttk.Scrollbar(show_data_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_data_frame, orient=VERTICAL)

        self.data_4_deatlis = ttk.Treeview(show_data_frame, columns=("emp_id", "emp_firstname", "emp_lastname", "emp_DOB", "emp_nid", "emp_phone", "emp_address", "department_name", "emp_reference", "emp_join_date", "emp_salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.data_4_deatlis.xview)
        scroll_y.config(command=self.data_4_deatlis.yview)

        self.data_4_deatlis.heading("emp_id", text="ID")
        self.data_4_deatlis.heading("emp_firstname", text="First Name")
        self.data_4_deatlis.heading("emp_lastname", text="Last Name")
        self.data_4_deatlis.heading("emp_DOB", text="Date Of Birth")
        self.data_4_deatlis.heading("emp_nid", text="NID No")
        self.data_4_deatlis.heading("emp_phone", text="Phone No")
        self.data_4_deatlis.heading("emp_address", text="Address")
        self.data_4_deatlis.heading("department_name", text="Department")
        self.data_4_deatlis.heading("emp_reference", text="Reference")
        self.data_4_deatlis.heading("emp_join_date", text="Join Date")
        self.data_4_deatlis.heading("emp_salary", text="Salary")
        self.data_4_deatlis["show"]="headings"


        self.data_4_deatlis.column('emp_id', width=10)
        self.data_4_deatlis.column('emp_firstname', width=10)
        self.data_4_deatlis.column('emp_lastname', width=10)
        self.data_4_deatlis.column('emp_DOB', width=10)
        self.data_4_deatlis.column('emp_nid', width=10)
        self.data_4_deatlis.column('emp_phone', width=10)
        self.data_4_deatlis.column('emp_address', width=10)
        self.data_4_deatlis.column('department_name', width=10)
        self.data_4_deatlis.column('emp_reference', width=10)
        self.data_4_deatlis.column('emp_join_date', width=10)
        self.data_4_deatlis.column('emp_salary', width=10)

        self.data_4_deatlis.pack(fill=BOTH, expand=1)

        # #   ========================  total amount view ========================
        # total_frame_ricived = Frame(table_frame, bd=2, relief="groove")
        # total_frame_ricived.place(x=685, y=358, width=250, height=33)
        # total_frame_cost = Frame(table_frame, bd=2, relief="groove")
        # total_frame_cost.place(x=940, y=358, width=250, height=33)
        # total_amount = db.search_dataToDate_total_amount(t_name, date, toDate, 'CD')
        # lbl_total = Label(total_frame_ricived, text="Total Ricived:", font=("times new roman",15, "bold"))
        # lbl_total.grid(row=0, column=0)
        # lbl_total = Label(total_frame_ricived, text=total_amount[0][0], font=("times new roman",15, "bold"))
        # lbl_total.grid(row=0, column=1)
        # lbl_total = Label(total_frame_cost, text="Total Cost:", font=("times new roman",15, "bold"))
        # lbl_total.grid(row=0, column=0)
        # lbl_total = Label(total_frame_cost, text=total_amount[0][1], font=("times new roman",15, "bold"))
        # lbl_total.grid(row=0, column=1)

    
    #   ======================== search one employee ========================
    def search_one_employee(self):
        emp_id = self.combobox_search_emp_Id.get()
        if emp_id == "Select ID":
            messagebox.showerror("Error", "Please, Provide the employee id!", parent=self.root)
        else:
            try:
                employee = db.search_employee(emp_id)
                self.view_teble()
                self.data_4_deatlis.delete(*self.data_4_deatlis.get_children())
                for i in employee:
                    self.data_4_deatlis.insert("", END, values=i)
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)
    #   ======================== search all employee ========================
    def search_all_employee(self):
        try:
            employee = db.search_employee('All')
            self.view_teble()
            self.data_4_deatlis.delete(*self.data_4_deatlis.get_children())
            for i in employee:
                self.data_4_deatlis.insert("", END, values=i)
        except Exception as ex:
            messagebox.showerror("Error", f"{ex}", parent=self.root)
    
    
     # =============================== clear frame =====================
    def clear_func(self):
        #   ========================  body image ========================
        clear_frame = Frame(self.root)
        clear_frame.place(x=0, y=85, width=1210, height=475)
        body_img = Image.open("images/promotion.jpeg")
        body_img = body_img.resize((1210, 475))
        self.photoBodyImg = ImageTk.PhotoImage(body_img)
        bodyLblImg = Label(clear_frame, image=self.photoBodyImg, bd=4, relief="groove")
        bodyLblImg.place(x=0, y=0, width=1210, height=475)
    



if __name__ == "__main__":
    root = Tk()
    obj = View_Promotion(root)
    root.mainloop()