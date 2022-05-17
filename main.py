from tkinter import *
from PIL import Image, ImageTk
from credit import Credit_win
from debit import Debit_win
from search import search_win
from blance import blance_win
from MyDB import Mydatabase
from tkinter import messagebox


class OfficeManagementSystem:
    def __init__(self, root):
    #   ========================  root icon title========================
        global db    
        db = Mydatabase()
        self.root = root
        self.root.title("Office Management System")
        self.root.geometry("1550x800+0+0")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))
        
    #   ========================  Top Image ========================

        top_img = Image.open("images/damo.jpg")
        top_img = top_img.resize((1550, 140))#, Image.ANTIALIAS
        self.photoTopImg = ImageTk.PhotoImage(top_img)
        topLblImg = Label(self.root, image=self.photoTopImg, bd=4, relief="groove").place(x=0, y=0, width=1550, height=110)
        
    #   ========================  Logo Image  ========================
        
        logo_img = Image.open("images/logo.jpg")
        logo_img = logo_img.resize((230, 140))
        self.photoLogoImg = ImageTk.PhotoImage(logo_img)
        logoLblImg = Label(self.root, image=self.photoLogoImg, bd=4, relief="groove").place(x=0, y=0, width=230, height=110)

    #   ========================  Title  ========================

        lbl_title = Label(self.root, text="OFFICE MANAGEMENT SYSTEM", font=("times new roman",40,"bold"), bg="#03396c", fg="#eeeeee", bd=4, relief="groove").place(x=0 , y=110, width=1550, height=70 )

    #   ========================  main Frame  ========================

        main_frame = Frame(self.root, bd=4, relief="groove", bg="#eeeeee")
        main_frame.place(x=0, y=180, width=1550, height=550)

    #   ========================  blance button ========================
        blance_button = Button(main_frame, text="$ Cash Blance", font=("times new roman",15,"bold"), bg="#f6cd61", fg="#2a4d69", bd=2, relief="groove", cursor="hand2", command=self.blance_func)
        blance_button.place(x=0, y=0, width=150, height=40)

    #   ========================  cash menu ========================
        lbl_cash = Label(main_frame, text="Cash Menu", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=4, relief="groove")
        lbl_cash.place(x=0, y=40, width=150, height=40)

    #   ========================  cash button frame ========================

        cash_btn_frame = Frame(main_frame, bd=4, relief="groove")
        cash_btn_frame.place(x=0, y=80, width=150, height=115) 

        credit_btn = Button(cash_btn_frame, text="Credit", command=self.credit_details, bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        credit_btn.place(x=0, y=0, width=140, height=35)
        debit_btn = Button(cash_btn_frame, text="Debit ", command=self.debit_details, bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        debit_btn.place(x=0, y=35, width=140, height=35)
        search_btn = Button(cash_btn_frame, text="Search ", command=self.search_details,  bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        search_btn.place(x=0, y=70, width=140, height=35)
    
    #   ========================  bank menu ========================
        lbl_bank = Label(main_frame, text="Bank Menu", font=("times new roman",20,"bold"), bg="#03396c", fg="#eeeeee", bd=4, relief="groove")
        lbl_bank.place(x=0, y=195, width=150, height=40)
    
    
#     #   ========================  Bank button frame ========================

        bank_btn_frame = Frame(main_frame, bd=4, relief="groove")
        bank_btn_frame.place(x=0, y=235, width=150, height=115) 

        bank_btn_1 = Button(bank_btn_frame, text="Button-1", bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        bank_btn_1.place(x=0, y=0, width=140, height=35)
        bank_btn_2 = Button(bank_btn_frame, text="Button-2", bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        bank_btn_2.place(x=0, y=35, width=140, height=35)
        bank_btn_3 = Button(bank_btn_frame, text="Button-3", bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        bank_btn_3.place(x=0, y=70, width=140, height=35)
    
#     #   ========================  salary menu ========================
        lbl_salary = Label(main_frame, text="Salary Menu", font=("times new roman",18,"bold"), bg="#03396c", fg="#eeeeee", bd=4, relief="groove")
        lbl_salary.place(x=0, y=350, width=150, height=40)
    
    
#     #   ========================  salary button frame ========================

        salary_btn_frame = Frame(main_frame, bd=4, relief="groove")
        salary_btn_frame.place(x=0, y=390, width=150, height=115) 

        salary_btn_1 = Button(salary_btn_frame, text="Button-1", bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        salary_btn_1.place(x=0, y=0, width=140, height=35)
        salary_btn_2 = Button(salary_btn_frame, text="Button-2", bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        salary_btn_2.place(x=0, y=35, width=140, height=35)
        salary_btn_3 = Button(salary_btn_frame, text="Button-3", bg="#6497b1", fg="#ffffff" ,font=("times new roman",15,"bold"), bd=1, cursor="hand2")
        salary_btn_3.place(x=0, y=70, width=140, height=35)

    #   ========================  body image ========================
        body_img = Image.open("images/body.jpg")
        body_img = body_img.resize((1320, 620))
        self.photoBodyImg = ImageTk.PhotoImage(body_img)
        bodyLblImg = Label(main_frame, image=self.photoBodyImg, bd=4, relief="groove")
        bodyLblImg.place(x=150, y=0, width=1330, height=620)
#   ========================  blance button ========================
    def blance_func(self):
        self.blance_new_win = Toplevel(self.root)
        self.blance_app = blance_win(self.blance_new_win)
        
        

#   ========================  credit function ========================
    def credit_details(self):
        self.credit_new_win = Toplevel(self.root)
        self.credit_app = Credit_win(self.credit_new_win)


#   ========================  Debit function ========================
    def debit_details(self):
        self.debit_new_win = Toplevel(self.root)
        self.debit_app = Debit_win(self.debit_new_win)
#   ========================  Debit function ========================
    def search_details(self):
        self.search_new_win = Toplevel(self.root)
        self.search_app = search_win(self.search_new_win)



if __name__ == "__main__":
    root = Tk()
    obj = OfficeManagementSystem(root)
    root.mainloop()
