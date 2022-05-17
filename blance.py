from tkinter import *
from MyDB import Mydatabase



class blance_win:
    def __init__(self, root):
        db = Mydatabase()
        self.root = root
        self.root.title("Blance")
        self.root.geometry("250x125+532+313")
        self.root.iconphoto(False,PhotoImage(file="images/icon.png"))


        #   ========================  Title  ========================

        blance_lbl_title = Label(self.root, text="BLANCE CHECK", font=("times new roman",15,"bold"), bg="#03396c", fg="#eeeeee", bd=2, relief="groove")
        blance_lbl_title.place(x=0 , y=0, width=250, height=40 )
        blance = db.check_blance()
        if blance < 1000:
            f_color = "#fe4a49"
        elif blance >= 1000 and blance <= 50000:
            f_color = "#f37736"
        elif blance > 50000 and blance <= 100000:
            f_color = "#2ab7ca"
        elif blance > 100000:
            f_color = "#7bc043"
        
        blance_lbl = Label(self.root, text="BDT: "+str(blance), font=("times new roman",20,"bold"), bd=2, relief="groove", bg=f_color)
        blance_lbl.place(x=0, y=40, width=250, height=40)

        exit_btn = Button(self.root, text="OK", font=("times new roman",10,"bold"), bd=2, relief="groove", bg="#03396c", fg="#eeeeee", command=self.end_func)
        exit_btn.place(x=150, y=90, width=70, height=25)

    def end_func(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = blance_win(root)
    root.mainloop()