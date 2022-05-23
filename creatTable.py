from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry #pip install tkcalender
from PIL import Image, ImageTk
from MyDB import Mydatabase


class CreatTable_win:
    def __init__(self, root):
        global db
        db = Mydatabase()
        self.root = root
        self.root.title("Creat Table")
        self.root.geometry("400x215+550+250")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))


        #   ========================  Title  ========================

        credit_lbl_title = Label(self.root, text="CREATE TABLE", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove")
        credit_lbl_title.place(x=0 , y=0, width=400, height=25 )

        #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((30, 25))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=0, relief="groove")
        logoLblImg.place(x=0, y=0, width=30, height=25)

        #   ========================  variable   ========================
        self.table_name = StringVar()
        self.table_type = StringVar()
        #   ========================  Lable frame  ========================

        from_lbl_frame = LabelFrame(self.root, text="Create Table", font=("times new roman",20,"bold"), bd=2, relief="groove")
        from_lbl_frame.place(x=10, y=25, width=380, height=180)

        lbl_table_name = Label(from_lbl_frame, text="Table Name :", font=("times new roman",15,"bold"))
        lbl_table_name.grid(row=0, column=0, padx=15, pady=10)
        entry_table_name = ttk.Entry(from_lbl_frame, font=("times new roman",15), textvariable=self.table_name)
        entry_table_name.grid(row=0, column=1, pady=10)

        lbl_table_type = Label(from_lbl_frame, justify=LEFT, anchor="w", text="Table Type : ", font=("times new roman",15,"bold"))
        lbl_table_type.grid(row=1, column=0, padx=15, pady=10)
        type_name = ["Credit", "Debit", "Credit & Debit"]
        combobox_table_type = ttk.Combobox(from_lbl_frame, values= type_name, font=("times new roman",14), state='readonly', textvariable=self.table_type)
        combobox_table_type.grid(row=1, column=1, pady=10)
        combobox_table_type.set("Select Type")

        sub_btn = Button(from_lbl_frame, text="Submit", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove", command=self.create_func)
        sub_btn.place(x=278, y=100, width=78, height=40)

    # =============================== submit function =====================
    def create_func(self):
        new_table_name = self.table_name.get()
        new_table_type = self.table_type.get()
        if new_table_type == "Select Type":
            messagebox.showerror("Error", "Please, select table type!", parent=self.root)
        elif new_table_name == "":
            messagebox.showerror("Error", "Please, Provide the table name!", parent=self.root)
        else:
            try:
                db.create_table(new_table_name, new_table_type)
                messagebox.showinfo("Success", "Successfully create table.\nName : {}\nType : {}".format(new_table_name, new_table_type), parent=self.root)
                self.root.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"{ex}", parent=self.root)










if __name__ == "__main__":
    root = Tk()
    obj = CreatTable_win(root)
    root.mainloop()