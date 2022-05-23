from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkcalendar import DateEntry #pip install tkcalender
from PIL import Image, ImageTk
from MyDB import Mydatabase




class Employee_win:
    def __init__(self, root):
        global db
        db = Mydatabase()
        self.root = root
        self.root.title("Employee")
        self.root.geometry("1210x550+155+170")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))


        #   ========================  Title  ========================

        employee_lbl_title = Label(self.root, text="ADD EMPLOYEE DATA DETAILS", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove")
        employee_lbl_title.place(x=0 , y=0, width=1210, height=40 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((80, 40))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove")
        logoLblImg.place(x=0, y=0, width=80, height=40)

        #   ========================  body image ========================
        body_image_frame = Frame(self.root)
        body_image_frame.place(x=0, y=85, width=1210, height=475)
        body_img = Image.open("images/employee.jpg")
        body_img = body_img.resize((1210, 475))
        self.photoBodyImg = ImageTk.PhotoImage(body_img)
        bodyLblImg = Label(body_image_frame, image=self.photoBodyImg, bd=4, relief="groove")
        bodyLblImg.place(x=0, y=0, width=1210, height=475)


        #   ========================  button frame Image  ========================
        btn_frame = Frame(self.root, bd=2, relief="groove")
        btn_frame.place(x=0, y=40, width=1210, height=45)
        #   ========================  button  Image  ========================
        advance_salary = Button(btn_frame, text="Payment Salary", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.payment_salary)
        advance_salary.grid(row=0, column=0, padx=5)


        add_emp = Button(btn_frame, text="Add Employee", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.add_employee)
        add_emp.grid(row=0, column=1, padx=5)


        advance_salary = Button(btn_frame, text="Advance Salary", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.advance_salary)
        advance_salary.grid(row=0, column=2, padx=5)
        

        add_dep = Button(btn_frame, text="Due Salary", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.due_salary)
        add_dep.grid(row=0, column=3, padx=5)

        add_dep = Button(btn_frame, text="Add Department", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.department_add)
        add_dep.grid(row=0, column=4, padx=5)



        #   ======================== add department variable   ========================
        self.department_name = StringVar()


        #   ======================== add employye variable   ========================
        self.emp_id = IntVar()
        self.emp_f_name = StringVar()
        self.emp_l_name = StringVar()
        self.emp_nid = StringVar()
        self.emp_phone = StringVar()
        self.emp_address = StringVar()
        self.emp_dep = StringVar()
        self.emp_ref = IntVar()
        self.emp_salary = IntVar()
        # self.emp_due_salary = IntVar()
        # self.emp_adv_salary = IntVar()

        #   ======================== advance salary variable   ========================
        self.adv_emp_month = StringVar()
        self.adv_emp_year = IntVar()
        self.adv_emp_id = StringVar()
        self.adv_emp_amount = IntVar()
        self.adv_new_emp = IntVar()


        #   ======================== due salary variable   ========================
        self.due_emp_month = StringVar()
        self.due_emp_year = IntVar()
        self.due_emp_id = StringVar()
        self.due_emp_amount = IntVar()

        #   ======================== salary variable   ========================
        self.sal_emp_id = StringVar()
        self.sal_emp_work = IntVar()
        self.sal_emp_attaen = IntVar()
        self.sal_month = StringVar()
        #   ======================== payment salary variable   ========================
        self.payment_value = IntVar()
    



    #   ======================== add employee function ========================
    def add_employee(self):
        self.clear_func()
    #   ========================  create lable frame add employee ========================
        lbl_frame = LabelFrame(self.root, text="Employee Details",font=("times new roman",20,"bold"), bd=2, relief="groove")
        lbl_frame.place(x=150, y=150, width=920, height=320)


        lbl_emp_id = Label(lbl_frame, text="Employee ID :*", font=("times new roman",15,"bold"))
        lbl_emp_id.grid(row=0, column=0, pady=5, padx=30)
        entry_emp_id = ttk.Spinbox(lbl_frame, from_=100, to=9999, font=("times new roman",15), textvariable=self.emp_id)
        entry_emp_id.grid(row=0, column=1, pady=5, padx=5)


        lbl_f_name = Label(lbl_frame, text="First Name :*", font=("times new roman",15,"bold"))
        lbl_f_name.grid(row=1, column=0, pady=5, padx=30)
        entry_f_name = ttk.Entry(lbl_frame, font=("times new roman",15), textvariable=self.emp_f_name)
        entry_f_name.grid(row=1, column=1, pady=5, padx=5, ipadx=7)


        lbl_l_name = Label(lbl_frame, text="Last Name :*", font=("times new roman",15,"bold"))
        lbl_l_name.grid(row=2, column=0, pady=5, padx=30)
        entry_l_name = ttk.Entry(lbl_frame, font=("times new roman",15), textvariable=self.emp_l_name)
        entry_l_name.grid(row=2, column=1, pady=5, padx=5, ipadx=7)


        lbl_DOB = Label(lbl_frame, text="Date of birth :*", font=("times new roman",15,"bold"))
        lbl_DOB.grid(row=3, column=0, pady=5, padx=30)
        self.entry_DOB = DateEntry(lbl_frame,state="readonly",selectmode='day', font=("times new roman",15) ,date_pattern="yyyy-mm-dd")
        self.entry_DOB.grid(row=3, column=1, pady=5, padx=5, ipadx=38)
        

        lbl_emp_nid = Label(lbl_frame, text="NID/DOB No :*", font=("times new roman",15,"bold"))
        lbl_emp_nid.grid(row=4, column=0, pady=5, padx=30)
        entry_emp_nid = ttk.Entry(lbl_frame, font=("times new roman",15), textvariable=self.emp_nid)
        entry_emp_nid.grid(row=4, column=1, pady=5, padx=5, ipadx=7)


        lbl_emp_phone = Label(lbl_frame, text="Phone No :*", font=("times new roman",15,"bold"))
        lbl_emp_phone.grid(row=0, column=3, pady=5, padx=30)
        entry_emp_phone = ttk.Entry(lbl_frame, font=("times new roman",15), textvariable=self.emp_phone)
        entry_emp_phone.grid(row=0, column=4, pady=5, padx=5, ipadx=7)


        lbl_address = Label(lbl_frame, text="Full Address :*", font=("times new roman",15,"bold"))
        lbl_address.grid(row=1, column=3, pady=5, padx=30)
        entry_address = ttk.Entry(lbl_frame, font=("times new roman",15), textvariable=self.emp_address)
        entry_address.grid(row=1, column=4, pady=5, padx=5, ipadx=7)

        dep_name = db.fatch_department_name()
        lbl_dep = Label(lbl_frame, text="Department :*", font=("times new roman",15,"bold"))
        lbl_dep.grid(row=2, column=3, pady=5, padx=30)
        entry_dep = ttk.Combobox(lbl_frame, values=dep_name, font=("times new roman",13, "bold"), state='readonly', textvariable=self.emp_dep)
        entry_dep.set("Select Department")
        entry_dep.grid(row=2, column=4, pady=5, padx=5, ipadx=7, ipady=2)


        ref_id = db.fatch_employee_id()
        lbl_emp_ref = Label(lbl_frame, text="Reference ID :", font=("times new roman",15,"bold"))
        lbl_emp_ref.grid(row=3, column=3, pady=5, padx=30)
        entry_ref = ttk.Combobox(lbl_frame, values=ref_id, font=("times new roman",13, "bold"), state='readonly', textvariable=self.emp_ref)
        entry_ref.set("Select ID")
        entry_ref.grid(row=3, column=4, pady=5, padx=5, ipadx=7, ipady=2)


        lbl_emp_salary = Label(lbl_frame, text="Salary*:", font=("times new roman",15,"bold"))
        lbl_emp_salary.grid(row=4, column=3, pady=5, padx=30)
        entry_emp_salary = ttk.Spinbox(lbl_frame, from_=0, to=99999999, font=("times new roman",15), textvariable=self.emp_salary)
        entry_emp_salary.grid(row=4, column=4, pady=5, padx=5)


        # lbl_emp_due_salary = Label(lbl_frame, text="Due Salary:", font=("times new roman",15,"bold"))
        # lbl_emp_due_salary.grid(row=4, column=3, pady=5, padx=30)
        # entry_emp_due_salary = ttk.Spinbox(lbl_frame, from_=0, to=99999999, font=("times new roman",15), textvariable=self.emp_due_salary)
        # entry_emp_due_salary.grid(row=4, column=4, pady=5, padx=5)


        # lbl_emp_adv_salary = Label(lbl_frame, text="Advance Salary:", font=("times new roman",15,"bold"))
        # lbl_emp_adv_salary.grid(row=5, column=3, pady=5, padx=30)
        # entry_emp_adv_salary = ttk.Spinbox(lbl_frame, from_=0, to=99999999, font=("times new roman",15), textvariable=self.emp_adv_salary)
        # entry_emp_adv_salary.grid(row=5, column=4, pady=5, padx=5)

        # ======================== button ========================
        btn_frame = Frame(lbl_frame, bd=2, relief="groove")
        btn_frame.place(x=320, y=220, width=315, height=45)
        emp_sub = Button(btn_frame, text="Submit", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=self.add_employee_data)
        emp_sub.place(x=160, y=1, width=150, height=38)
        emp_from_clear = Button(btn_frame, text="Clare", font=("times new roman",15,"bold"), bg="#fe4a49", fg="#eeeeee", bd=2, relief="groove", command=self.add_employee)
        emp_from_clear.place(x=0, y=1, width=150, height=38)


     # =============================== add employee data function =====================
    def add_employee_data(self):
        id = self.emp_id.get()
        f_name = self.emp_f_name.get()
        l_name = self.emp_l_name.get()
        dob = self.entry_DOB.get_date()
        nid_no = self.emp_nid.get()
        phone_no = self.emp_phone.get()
        address = self.emp_address.get()
        dep = self.emp_dep.get()
        ref = self.emp_ref.get()
        salary = self.emp_salary.get()
        # d_salary = self.emp_due_salary.get()
        # a_salary = self.emp_adv_salary.get()
        if id == 0:
            messagebox.showerror("Error", "Please, Provide the employee id!", parent=self.root)
        elif f_name == "":
            messagebox.showerror("Error", "Please, Provide the employee first name!", parent=self.root)
        elif l_name == "":
            messagebox.showerror("Error", "Please, Provide the employee last name!", parent=self.root)
        elif nid_no == 0:
            messagebox.showerror("Error", "Please, Provide the employee NID no!", parent=self.root)
        elif phone_no == "":
            messagebox.showerror("Error", "Please, Provide the employee phone no!", parent=self.root)
        elif address == "":
            messagebox.showerror("Error", "Please, Provide the employee full address!", parent=self.root)
        elif dep == "Select Department":
            messagebox.showerror("Error", "Please, Select the employee department!", parent=self.root)
        elif salary == 0:
            messagebox.showerror("Error", "Please, Provide the employee Salary!", parent=self.root)
        else:
            try:
                if ref == "Select ID":
                    ref = 0
                db.add_employee(id, f_name, l_name, dob, nid_no, phone_no, address, dep, int(ref), salary)
                messagebox.showinfo("Success", "Successfully submitted emoloyee", parent=self.root)
                self.add_employee()
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)


    #   ========================  create function ========================
    def department_add(self):
        self.clear_func()
        from_lbl_frame = LabelFrame(self.root, text="Create Department", font=("times new roman",20,"bold"), bd=2, relief="groove")
        from_lbl_frame.place(x=385, y=185, width=440, height=180)

        lbl_department_name = Label(from_lbl_frame, text="Department Name :", font=("times new roman",15,"bold"))
        lbl_department_name.place(x=10, y=30, width=200, height=40)
        entry_department_name = ttk.Entry(from_lbl_frame, font=("times new roman",15), textvariable=self.department_name)
        entry_department_name.place(x=220, y=30, width=180, height=30)

        sub_btn = Button(from_lbl_frame, text="Submit", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove", command=self.dep_submit_func)
        sub_btn.place(x=278, y=90, width=78, height=40)

     # =============================== department submit function =====================
    def dep_submit_func(self):
        new_department_name = self.department_name.get()
        if new_department_name == "":
            messagebox.showerror("Error", "Please, Provide the department name!", parent=self.root)
        else:
            try:
                db.add_department(new_department_name)
                messagebox.showinfo("Success", "Successfully submitted department name \"{}\"".format(new_department_name), parent=self.root)
                self.department_add()
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)
    
     # =============================== advance salary frame =====================
    def advance_salary(self):
        self.clear_func()
        adv_lbl_frame = LabelFrame(self.root, text="Advance Salary", font=("times new roman",20,"bold"), bd=2, relief="groove")
        adv_lbl_frame.place(x=385, y=125, width=450, height=350)


        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        pay_sal_lbl_month = Label(adv_lbl_frame, text="Advance Month :", font=("times new roman",15,"bold"))
        pay_sal_lbl_month.grid(row=0, column=0, pady=20, padx=20)
        pay_sal_entry_month = ttk.Combobox(adv_lbl_frame, values=month, font=("times new roman",13, "bold"), state='readonly', textvariable=self.adv_emp_month)
        pay_sal_entry_month.set("Select Month")
        pay_sal_entry_month.grid(row=0, column=1, pady=5, padx=5, ipadx=7, ipady=2)


        year = [i for i in range(2022, 2032)]
        pay_sal_lbl_month = Label(adv_lbl_frame, text="Advance Year :", font=("times new roman",15,"bold"))
        pay_sal_lbl_month.grid(row=1, column=0, pady=5, padx=20)
        pay_sal_entry_month = ttk.Combobox(adv_lbl_frame, values=year, font=("times new roman",13, "bold"), state='readonly', textvariable=self.adv_emp_year)
        pay_sal_entry_month.set("Select Year")
        pay_sal_entry_month.grid(row=1, column=1, pady=5, padx=5, ipadx=7, ipady=2)



        # lbl_date = Label(adv_lbl_frame, text="Date :", font=("times new roman",15,"bold"))
        # lbl_date.grid(row=0, column=0, pady=20, padx=20)
        # self.entry_date = DateEntry(adv_lbl_frame,state="readonly",selectmode='day', font=("times new roman",15) ,date_pattern="yyyy-mm-dd")
        # self.entry_date.grid(row=0, column=1, pady=5, padx=5, ipadx=38)


        emp_id = db.fatch_employee_id()
        lbl_emp_id = Label(adv_lbl_frame, text="Employee ID :", font=("times new roman",15,"bold"))
        lbl_emp_id.grid(row=2, column=0, pady=20, padx=20)
        entry_emp_id = ttk.Combobox(adv_lbl_frame, values=emp_id, font=("times new roman",13, "bold"), state='readonly', textvariable=self.adv_emp_id)
        entry_emp_id.set("Select ID")
        entry_emp_id.grid(row=2, column=1, pady=20, padx=5, ipadx=7, ipady=2)


        lbl_emp_adv_amount = Label(adv_lbl_frame, text="Advance Amount :", font=("times new roman",15,"bold"))
        lbl_emp_adv_amount.grid(row=3, column=0, pady=5, padx=20)
        entry_emp_adv_amount = ttk.Spinbox(adv_lbl_frame, from_=0, to=99999999, font=("times new roman",15), textvariable=self.adv_emp_amount)
        entry_emp_adv_amount.grid(row=3, column=1, pady=5, padx=5)

     
        entry_emp_adv_amount = ttk.Checkbutton(adv_lbl_frame, text="New employee advance salary.", variable=self.adv_new_emp)
        entry_emp_adv_amount.place(x=205, y=230)


        sub_btn_sel = Button(adv_lbl_frame, text="Submit", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove", command=self.advance_salary_func)
        sub_btn_sel.place(x=330, y=260, width=80, height=40)


        sub_btn_sel = Button(adv_lbl_frame, text="Clear", font=("times new roman",15,"bold"), bg="#fe4a49", fg="#eeeeee", bd=2, relief="groove", command=self.advance_salary)
        sub_btn_sel.place(x=230, y=260, width=80, height=40) 

     # =============================== clear frame =====================
    def advance_salary_func(self):
        month = self.adv_emp_month.get()
        year = self.adv_emp_year.get()
        emp_id = self.adv_emp_id.get()
        amount = self.adv_emp_amount.get()
        new_old = self.adv_new_emp.get()
        print(type(new_old))
        if emp_id == 'Select ID':
            messagebox.showerror("Error", "Please, Select the employee id!", parent=self.root)
        elif amount == 0:
            messagebox.showerror("Error", "Please, Provide the advance amount!", parent=self.root)
        elif year == "Select Year":
            messagebox.showerror("Error", "Please, Select the year!", parent=self.root)
        elif month == "Select Month":
            messagebox.showerror("Error", "Please, Select the month!", parent=self.root)
        else:
            try:
                db.add_advance_salary(month, int(year), amount, int(emp_id), new_old)
                messagebox.showinfo("Success", "Successfully submitted advance salary")
                self.advance_salary()
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)

     # =============================== due salary frame =====================
    def due_salary(self):
        self.clear_func()
        deu_lbl_frame = LabelFrame(self.root, text="Due Salary", font=("times new roman",20,"bold"), bd=2, relief="groove")
        deu_lbl_frame.place(x=385, y=135, width=450, height=330)


        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        deu_sal_lbl_month = Label(deu_lbl_frame, text="Advance Month :", font=("times new roman",15,"bold"))
        deu_sal_lbl_month.grid(row=0, column=0, pady=20, padx=20)
        deu_sal_entry_month = ttk.Combobox(deu_lbl_frame, values=month, font=("times new roman",13, "bold"), state='readonly', textvariable=self.due_emp_month)
        deu_sal_entry_month.set("Select Month")
        deu_sal_entry_month.grid(row=0, column=1, pady=5, padx=5, ipadx=7, ipady=2)


        year = [i for i in range(2022, 2032)]
        deu_sal_lbl_month = Label(deu_lbl_frame, text="Advance Year :", font=("times new roman",15,"bold"))
        deu_sal_lbl_month.grid(row=1, column=0, pady=5, padx=20)
        deu_sal_entry_month = ttk.Combobox(deu_lbl_frame, values=year, font=("times new roman",13, "bold"), state='readonly', textvariable=self.due_emp_year)
        deu_sal_entry_month.set("Select Year")
        deu_sal_entry_month.grid(row=1, column=1, pady=5, padx=5, ipadx=7, ipady=2)



        # lbl_date = Label(adv_lbl_frame, text="Date :", font=("times new roman",15,"bold"))
        # lbl_date.grid(row=0, column=0, pady=20, padx=20)
        # self.entry_date = DateEntry(adv_lbl_frame,state="readonly",selectmode='day', font=("times new roman",15) ,date_pattern="yyyy-mm-dd")
        # self.entry_date.grid(row=0, column=1, pady=5, padx=5, ipadx=38)


        emp_id = db.fatch_employee_id()
        lbl_emp_id = Label(deu_lbl_frame, text="Employee ID :", font=("times new roman",15,"bold"))
        lbl_emp_id.grid(row=2, column=0, pady=20, padx=20)
        entry_emp_id = ttk.Combobox(deu_lbl_frame, values=emp_id, font=("times new roman",13, "bold"), state='readonly', textvariable=self.due_emp_id)
        entry_emp_id.set("Select ID")
        entry_emp_id.grid(row=2, column=1, pady=20, padx=5, ipadx=7, ipady=2)


        lbl_emp_deu_amount = Label(deu_lbl_frame, text="Advance Amount :", font=("times new roman",15,"bold"))
        lbl_emp_deu_amount.grid(row=3, column=0, pady=5, padx=20)
        entry_emp_deu_amount = ttk.Spinbox(deu_lbl_frame, from_=0, to=99999999, font=("times new roman",15), textvariable=self.due_emp_amount)
        entry_emp_deu_amount.grid(row=3, column=1, pady=5, padx=5)


        sub_btn_sel = Button(deu_lbl_frame, text="Submit", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove", command=self.due_salary_func)
        sub_btn_sel.place(x=330, y=230, width=80, height=40)


        sub_btn_sel = Button(deu_lbl_frame, text="Clear", font=("times new roman",15,"bold"), bg="#fe4a49", fg="#eeeeee", bd=2, relief="groove", command=self.advance_salary)
        sub_btn_sel.place(x=230, y=230, width=80, height=40) 

     # =============================== clear frame =====================
    def due_salary_func(self):
        month = self.due_emp_month.get()
        year = self.due_emp_year.get()
        emp_id = int(self.due_emp_id.get())
        amount = self.due_emp_amount.get()
        if emp_id == 'Select ID':
            messagebox.showerror("Error", "Please, Select the employee id!", parent=self.root)
        elif amount == 0:
            messagebox.showerror("Error", "Please, Provide the due amount!", parent=self.root)
        elif year == "Select Year":
            messagebox.showerror("Error", "Please, Select the year!", parent=self.root)
        elif month == "Select Month":
            messagebox.showerror("Error", "Please, Select the month!", parent=self.root)
        else:
            try:
                db.add_due_salary(month, int(year), amount, int(emp_id))
                messagebox.showinfo("Success", "Successfully submitted advance salary")
                self.advance_salary()
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)

     # =============================== payment salary frame =====================
    def payment_salary(self):
        self.clear_func()
        adv_lbl_frame = LabelFrame(self.root, text="Advance Salary", font=("times new roman",20,"bold"), bd=2, relief="groove")
        adv_lbl_frame.place(x=385, y=135, width=450, height=380)


        lbl_date = Label(adv_lbl_frame, text="Date :", font=("times new roman",15,"bold"))
        lbl_date.grid(row=0, column=0, pady=20, padx=20)
        self.pay_sal_entry_date = DateEntry(adv_lbl_frame,state="readonly",selectmode='day', font=("times new roman",15) ,date_pattern="yyyy-mm-dd")
        self.pay_sal_entry_date.grid(row=0, column=1, pady=5, padx=5, ipadx=38)


        pay_sal_emp_id = db.fatch_employee_id()
        pay_sal_lbl_emp_id = Label(adv_lbl_frame, text="Employee ID :", font=("times new roman",15,"bold"))
        pay_sal_lbl_emp_id.grid(row=1, column=0, pady=5, padx=20)
        pay_sal_entry_emp_id = ttk.Combobox(adv_lbl_frame, values=pay_sal_emp_id, font=("times new roman",13, "bold"), state='readonly', textvariable=self.sal_emp_id)
        pay_sal_entry_emp_id.set("Select ID")
        pay_sal_entry_emp_id.grid(row=1, column=1, pady=5, padx=5, ipadx=7, ipady=2)


        pay_sal_lbl_work = Label(adv_lbl_frame, text="Working day :", font=("times new roman",15,"bold"))
        pay_sal_lbl_work.grid(row=2, column=0, pady=10, padx=20)
        pay_sal_entry_work = ttk.Spinbox(adv_lbl_frame, from_=0, to=30, font=("times new roman",15), textvariable=self.sal_emp_work)
        pay_sal_entry_work.grid(row=2, column=1, pady=10, padx=5)


        pay_sal_lbl_emp_atten = Label(adv_lbl_frame, text="Attendance day :", font=("times new roman",15,"bold"))
        pay_sal_lbl_emp_atten.grid(row=3, column=0, pady=10, padx=20)
        pay_sal_entry_emp_atten = ttk.Spinbox(adv_lbl_frame, from_=0, to=30, font=("times new roman",15), textvariable=self.sal_emp_attaen)
        pay_sal_entry_emp_atten.grid(row=3, column=1, pady=5, padx=5)

        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        pay_sal_lbl_month = Label(adv_lbl_frame, text="Payment month :", font=("times new roman",15,"bold"))
        pay_sal_lbl_month.grid(row=4, column=0, pady=5, padx=20)
        pay_sal_entry_month = ttk.Combobox(adv_lbl_frame, values=month, font=("times new roman",13, "bold"), state='readonly', textvariable=self.sal_month)
        pay_sal_entry_month.set("Select Month")
        pay_sal_entry_month.grid(row=4, column=1, pady=5, padx=5, ipadx=7, ipady=2)


        sub_btn = Button(adv_lbl_frame, text="Submit", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove", command=self.calculate_salary)
        sub_btn.place(x=330, y=280, width=80, height=40)


        sub_btn = Button(adv_lbl_frame, text="Clear", font=("times new roman",15,"bold"), bg="#fe4a49", fg="#eeeeee", bd=2, relief="groove", command=self.payment_salary)
        sub_btn.place(x=230, y=280, width=80, height=40) 



     # =============================== calculate_salary =====================
    def calculate_salary(self):
        global advance
        global due
        date = self.pay_sal_entry_date.get_date()
        emp_id = self.sal_emp_id.get()
        work = self.sal_emp_work.get()
        attaen = self.sal_emp_attaen.get()
        month = self.sal_month.get()
        if emp_id == 'Select ID':
            messagebox.showerror("Error", "Please, Provide the employee id!", parent=self.root)
        elif work == 0:
            messagebox.showerror("Error", "Please, Provide the working day!", parent=self.root)
        elif month == 'Select Month':
            messagebox.showerror("Error", "Please, Select the payment month!", parent=self.root)
        else:
            try:
                name_sal = db.fatch_name_employees(emp_id)
                adv_sel = db.fatch_adv_net_sel(emp_id, month)
                if adv_sel == None:
                    adv_sel = 0
                deu_sel = db.previous_month_sal(emp_id, month)
                if deu_sel == None:
                    deu_sel = 0
                emp_name = name_sal[0] + " " + name_sal[1]
                if adv_sel == 0 and deu_sel != 0:
                    net_salary = int(((int(name_sal[2]) / work) * attaen) + deu_sel)
                elif deu_sel == 0 and adv_sel != 0:
                    net_salary = int(((int(name_sal[2]) / work) * attaen) - int(adv_sel))
                elif adv_sel == 0 and deu_sel == 0:
                    net_salary = int((int(name_sal[2]) / work) * attaen)
                else:
                    net_salary = int((((int(name_sal[2]) / work) * attaen) - int(adv_sel)) + deu_sel)
                self.show_payment(emp_id, emp_name, work, attaen, month, adv_sel, deu_sel, net_salary)
                # print(type(name_sal), type(adv_sel), type(deu_sel))
                # print(name_sal, adv_sel, deu_sel, )
                    
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)
                


     # =============================== show payment salary  =====================
    def show_payment(self,emp_id, name, work, attaen, month, advance_net, due, net_salary):
        self.clear_func()
        print(advance_net, due)
    #   ========================  create lable frame add employee ========================
        sw_sel_frame = LabelFrame(self.root, text="Employee Details",font=("times new roman",20,"bold"), bd=2, relief="groove")
        sw_sel_frame.place(x=375, y=150, width=460, height=320)


        sw_sel_emp_name = Label(sw_sel_frame, text="Employee Name :", font=("times new roman",15,"bold"))
        sw_sel_emp_name.grid(row=0, column=0, pady=5, padx=30)
        valu_emp_name = Label(sw_sel_frame, text=name, font=("times new roman",15,"bold"), bd=2, relief="groove")
        valu_emp_name.grid(row=0, column=1, pady=5, padx=5, ipadx=5,ipady=2)

        sw_sel_emp_adv = Label(sw_sel_frame, text="Total Advance :", font=("times new roman",15,"bold"))
        sw_sel_emp_adv.grid(row=1, column=0, pady=5, padx=30)
        valu_emp_adv = Label(sw_sel_frame, text=advance_net, font=("times new roman",15,"bold"), bd=2, relief="groove")
        valu_emp_adv.grid(row=1, column=1, pady=5, padx=5, ipadx=5,ipady=2)

        sw_sel_emp_due = Label(sw_sel_frame, text="Total Due :", font=("times new roman",15,"bold"))
        sw_sel_emp_due.grid(row=2, column=0, pady=5, padx=30)
        valu_emp_due = Label(sw_sel_frame, text=due, font=("times new roman",15,"bold"), bd=2, relief="groove")
        valu_emp_due.grid(row=2, column=1, pady=5, padx=5, ipadx=5,ipady=2)

        sw_sel_emp_net = Label(sw_sel_frame, text="Net Salary :", font=("times new roman",15,"bold"))
        sw_sel_emp_net.grid(row=3, column=0, pady=5, padx=30)
        valu_emp_net = Label(sw_sel_frame, text=net_salary, font=("times new roman",15,"bold"), bd=2, relief="groove")
        valu_emp_net.grid(row=3, column=1, pady=5, padx=5, ipadx=5,ipady=2)

        sw_sel_emp_pay = Label(sw_sel_frame, text="Net Salary :", font=("times new roman",15,"bold"))
        sw_sel_emp_pay.grid(row=4, column=0, pady=5, padx=30)
        valu_emp_pay = ttk.Spinbox(sw_sel_frame, from_=0, to=9999999999, font=("times new roman",15), textvariable=self.payment_value)
        valu_emp_pay.grid(row=4, column=1, pady=5, padx=5)

        # ======================== button ========================
        btn_frame = Frame(sw_sel_frame, bd=2, relief="groove")
        btn_frame.place(x=72, y=220, width=315, height=45)
        emp_sub = Button(btn_frame, text="Submit", font=("times new roman",15,"bold"), bg="#7bc043", fg="#eeeeee", bd=2, relief="groove", command=lambda : self.salary_payment_data(emp_id, name, work, attaen, month, advance_net, due, net_salary))
        emp_sub.place(x=160, y=1, width=150, height=38)
        emp_from_clear = Button(btn_frame, text="Clare", font=("times new roman",15,"bold"), bg="#fe4a49", fg="#eeeeee", bd=2, relief="groove", command=self.add_employee)
        emp_from_clear.place(x=0, y=1, width=150, height=38)


     # =============================== add salary payment data =====================
    def salary_payment_data(self, emp_id, name, work, attaen, month, net_advance, due, net_salary):
        pay_amount = self.payment_value.get()
        if pay_amount <= 0:
            messagebox.showerror("Error", "Please, Provide the payment salary!", parent=self.root)
        else:
            try:
                db.add_salary_date(emp_id, name, work, attaen, month, net_advance, due, net_salary, pay_amount)
                messagebox.showinfo("Success", "Successfully submitted salary")
                if (net_salary - pay_amount) > 0:
                    messagebox.showinfo("Success", "Successfully submitted due amount! \n\n Amount : {}".format(net_salary - pay_amount))
                elif (net_salary - pay_amount) < 0:
                    messagebox.showinfo("Success", "Successfully submitted advance amount! \n\n Amount : {}".format(net_salary - pay_amount))

            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)



     # =============================== clear frame =====================
    def clear_func(self):
        #   ========================  body image ========================
        clear_frame = Frame(self.root)
        clear_frame.place(x=0, y=85, width=1210, height=475)
        # body_img = Image.open("images/employee.jpg")
        # body_img = body_img.resize((1210, 475))
        # self.photoBodyImg = ImageTk.PhotoImage(body_img)
        # bodyLblImg = Label(clear_frame, image=self.photoBodyImg, bd=4, relief="groove")
        # bodyLblImg.place(x=0, y=0, width=1210, height=475)

    

 




if __name__ == "__main__":
    root = Tk()
    obj = Employee_win(root)
    root.mainloop()









    # INSERT INTO `cash_book`.`employees` (`emp_id`, `emp_firstname`, `emp_lastname`, `emp_DOB`, `emp_nid`, `emp_phone`, `emp_address`, `department_name`, `emp_join_date`, `emp_salary`) VALUES ('101', 'x', 'y', '2002-5-14', '123456789', '01703081812', 'abc', 'Test', '2022-05-18', '30000');