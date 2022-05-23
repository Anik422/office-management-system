import re
import mysql.connector as connector



class Mydatabase:
    def __init__(self):
        #database cannect start
        self.mydb = connector.connect( 
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="cash_book"
        )
        #database cannect end

        
        # create all table query set start
        cur = self.mydb.cursor()
        create_dailay_account = "CREATE TABLE if not exists `Dailay Account`(Id int NOT NULL AUTO_INCREMENT unique , `Date`  DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int DEFAULT 0, Cost int DEFAULT 0, Blance int DEFAULT 0, cr_dr varchar(1) NOT NULL, PRIMARY KEY(Id));"
        cur.execute(create_dailay_account)
        debit_table_name = "CREATE TABLE if not exists `Debit Table Name` ( Id int AUTO_INCREMENT unique,`Name` varchar(500) NOT NULL, PRIMARY KEY(Id));"
        cur.execute(debit_table_name)
        credit_table_name = "CREATE TABLE if not exists `Credit Table Name` ( Id int AUTO_INCREMENT unique,`Name` varchar(500) NOT NULL, PRIMARY KEY(Id));"
        cur.execute(credit_table_name)
        create_department = "create table if not exists Department(`department_name` varchar(100) not null,primary key (`department_name`));"
        cur.execute(create_department)
        create_employees = """Create Table if not exists Employees(`emp_id` INT not null,`emp_firstname` varchar(100) not null,
                                `emp_lastname` varchar(100) not null,`emp_DOB` date not null,`emp_nid` varchar(15) not null,
                                `emp_phone` varchar(12) not null,`emp_address` varchar(255) not null,`department_name` varchar(100) not null,
                                `emp_reference` int default 0,`emp_join_date` datetime DEFAULT NOW(),`emp_salary` INT not null,
                                primary key(`emp_id`),UNIQUE KEY `employeeid_employee_UNIQUE` (`emp_id`),
                                foreign key(`department_name`) REFERENCES Department(`department_name`));"""
        cur.execute(create_employees)
        advance_salary = """CREATE TABLE if not exists `Advance Salary`
                            (
                                `ID` INT NOT NULL AUTO_INCREMENT UNIQUE,
                                `Date` DATETIME NOT NULL DEFAULT NOW(),
                                `Month` varchar(20) NOT NULL,
                                `Year` int NOT NULL,
                                `Amount` INT NOT NULL,
                                `Employee ID` INT NOT NULL,
                                PRIMARY KEY (`ID`),
                                FOREIGN KEY ( `Employee ID`) REFERENCES `employees`(`emp_id`)
                            );"""
        cur.execute(advance_salary)
        due_salary = """CREATE TABLE if not exists `Due Salary`
                            (
                                `ID` INT NOT NULL AUTO_INCREMENT UNIQUE,
                                `Date` DATETIME NOT NULL DEFAULT NOW(),
                                `Month` varchar(20) NOT NULL,
                                `Year` int NOT NULL,
                                `Amount` INT NOT NULL,
                                `Employee ID` INT NOT NULL,
                                PRIMARY KEY (`ID`),
                                FOREIGN KEY ( `Employee ID`) REFERENCES `employees`(`emp_id`)
                            );"""
        cur.execute(due_salary)
        salary_table = """CREATE TABLE if not exists `Salary`
                            (
                                `ID` INT NOT NULL AUTO_INCREMENT UNIQUE,
                                `Date` DATETIME NOT NULL DEFAULT NOW(),
                                `emp_id` INT NOT NULL,
                                `emp Name` varchar(200) NOT NULL,
                                `working day` INT NOT NULL,
                                `attendance day` INT NOT NULL,
                                `month` varchar(20) not null,
                                `net advance salary` int not null,
                                `net due salary` int not null,
                                `net salary` int not null,
                                `payment salary` int not null,
                                PRIMARY KEY (`ID`),
                                FOREIGN KEY ( `emp_id`) REFERENCES `employees`(`emp_id`)
                            );"""
        cur.execute(salary_table)
        # create_stationary = "CREATE TABLE if not exists `Stationary` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_stationary)
        # create_stationary = "CREATE TABLE if not exists `Stationary` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_stationary)
        # create_Office_Maintenance = "CREATE TABLE if not exists `Office Maintenance` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Office_Maintenance)
        # create_Dailay_Expendeture = "CREATE TABLE if not exists `Dailay Expendeture` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Dailay_Expendeture)
        # create_Convance  = "CREATE TABLE if not exists `Convance` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Convance)
        # create_TNT_Mobile_Bill_Office = "CREATE TABLE if not exists `TNT/Mobile Bill Office` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_TNT_Mobile_Bill_Office )
        # create_Courier = "CREATE TABLE if not exists `Courier` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Courier )
        # create_Gift = "CREATE TABLE if not exists `Gift` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Gift )
        # create_MD_Houae = "CREATE TABLE if not exists `MD Houae` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_MD_Houae )
        # create_MD_Houae_Baribadh = "CREATE TABLE if not exists `MD Houae Baribadh` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_MD_Houae_Baribadh )
        # create_MD_Car = "CREATE TABLE if not exists `MD Car` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_MD_Car)
        # create_MD_Mobil_BKash = "CREATE TABLE if not exists `MD Mobil & BKash` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_MD_Mobil_BKash)
        # create_MD_Credit_Card_Payment = "CREATE TABLE if not exists `MD Credit Card Payment` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_MD_Credit_Card_Payment)
        # create_Managing_Director = "CREATE TABLE if not exists `Managing Director`( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Managing_Director)
        # create_Fees_Tex = "CREATE TABLE if not exists `Fees & Tex` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Fees_Tex)
        # create_C_and_F = "CREATE TABLE if not exists `C & F` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_C_and_F)
        # create_Carring_Cost = "CREATE TABLE if not exists `Carring Cost` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Carring_Cost)
        # create_bill = "CREATE TABLE if not exists `Bill` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_bill)
        # create_rent_sever_office = "CREATE TABLE if not exists `RENT SEVER OFFICE` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_rent_sever_office)
        # create_rent_head_office = "CREATE TABLE if not exists `RENT HEAD OFFICE` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_rent_head_office)
        # create_Renewal_Fees = "CREATE TABLE if not exists `Renewal Fees` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Renewal_Fees)
        # create_Machinaries_setup_Maintenance = "CREATE TABLE if not exists `Tannery Machinaries setup and Maintenance` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        # cur.execute(create_Machinaries_setup_Maintenance)
        # global table_names_credit
        self.table_names_credit = ['Cash Receiv/Pay', 'Managing Director']
        self.table_names_debit = []
        # create all table query set end


    # ============================ create table ===========================
    def create_table(self, table_name, drcr):
        cur = self.mydb.cursor()
        if drcr == "Debit":
            create_table = "CREATE TABLE if not exists `{}` ( Id int NOT NULL AUTO_INCREMENT unique, `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );".format(table_name)
            table_name_query = "INSERT INTO `Debit Table Name`(Name) VALUES ('{}');".format(table_name)
            cur.execute(table_name_query)
            self.mydb.commit()
        elif drcr == "Credit":
            create_table = "CREATE TABLE if not exists `{}` ( Id int NOT NULL AUTO_INCREMENT unique, `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );".format(table_name)
            table_name_query = "INSERT INTO `Credit Table Name`(Name) VALUES ('{}');".format(table_name)
            cur.execute(table_name_query)
            self.mydb.commit()
        elif drcr == "Credit & Debit":
            create_table = "CREATE TABLE if not exists `{}`(Id int NOT NULL AUTO_INCREMENT unique , `Date`  DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int DEFAULT 0, Cost int DEFAULT 0, Blance int DEFAULT 0, cr_dr varchar(1) NOT NULL, PRIMARY KEY(Id));".format(table_name)
            table_name_debit = "INSERT INTO `Debit Table Name`(Name) VALUES ('{}');".format(table_name)
            table_name_credit = "INSERT INTO `Credit Table Name`(Name) VALUES ('{}');".format(table_name)
            cur.execute(table_name_debit)
            self.mydb.commit()
            cur.execute(table_name_credit)
            self.mydb.commit()
        cur.execute(create_table)

    # ============================ fatch table  name ===========================

    def fatch_table_name(self, crdr):
        cur = self.mydb.cursor()
        if crdr != "All":
            if crdr == "C":
                name_query = "SELECT `Name` FROM `credit table name`;"
            elif crdr == "D":
                name_query = "SELECT `Name` FROM `debit table name`;"
            cur.execute(name_query) 
            debit_credit_table = cur.fetchall()
            table_name = []
            for i in debit_credit_table:
                table_name.append(i[0])
            return table_name
        else:
            credit_name_query = "SELECT `Name` FROM `credit table name`;"
            debit_name_query = "SELECT `Name` FROM `debit table name`;"
            all_table_name = []
            cur.execute(credit_name_query) 
            all_cr_table = cur.fetchall()
            for i in all_cr_table:
                all_table_name.append(i[0])
            cur.execute(debit_name_query) 
            all_dr_table = cur.fetchall()
            for i in all_dr_table:
                all_table_name.append(i[0])
            return all_table_name


   


    # ============================ dailay account data entry===========================
    def table_data_entry(self, date, description, money, crDr, tableName ):
        global table_query
        print(date, description, money, crDr, tableName)
        #all table data insart start
        #credit Account data insart start     
        if crDr == 'C':      
            query = "INSERT INTO `Dailay Account`(`Date`, `Description`, Ricived, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, description, money, crDr)
            table_query = "INSERT INTO `{}`(`Date`, `Description`, Ricived, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(tableName, date, description, money, crDr)
            cur = self.mydb.cursor()
            cur.execute(table_query)
            self.mydb.commit()
            #debit Account data insart end
        #credit Account data insart end
     


        #debit Account data insart start
        elif crDr == 'D':
            if tableName == '':
                query = "INSERT INTO `Dailay Account`(`Date`, `Description`, Cost, cr_dr) VALUES (date(now()), '{}', {}, '{}');".format( description, money, crDr)
            else:    
                query = "INSERT INTO `Dailay Account`(`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, description, money, crDr)
                table_query = "INSERT INTO `{}`(`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( tableName,date, description, money, crDr)
                cur = self.mydb.cursor()
                cur.execute(table_query)
                self.mydb.commit()
            #debit Account data insart end
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        #all table data insart end

        #dailay_account table Blance column data insart query start
        query = "SELECT Id, Ricived, Cost, cr_dr FROM `Dailay Account` ORDER BY Id DESC LIMIT 1"
        cur.execute(query)
        last_id = []
        for i in cur:
            last_id.append(i)
        query = "select Blance from `Dailay Account` WHERE Id = {};".format((last_id[0][0]-1))
        cur.execute(query)
        for i in cur:
            last_id.append(i)
        # print(last_id)
        if last_id[0][3] == 'C':
            query = "UPDATE `Dailay Account` SET Blance = {} + {} WHERE Id = {};".format(last_id[0][1], last_id[1][0], last_id[0][0])
            cur.execute(query)
            self.mydb.commit()
        elif last_id[0][3] == 'D':
            query = "UPDATE `Dailay Account` SET Blance = {} - {} WHERE Id = {};".format(last_id[1][0], last_id[0][2], last_id[0][0])
            cur.execute(query)
            self.mydb.commit()
        #dailay_account table Blance column data insart query end
  


    # =================== add employee function =====================
    def add_employee(self, emp_id, emp_firstname, emp_lastname, emp_DOB, emp_nid, emp_phone, emp_address, department_name, emp_reference, emp_salary):
        query = "INSERT INTO `cash_book`.`employees` (`emp_id`, `emp_firstname`, `emp_lastname`, `emp_DOB`, `emp_nid`, `emp_phone`, `emp_address`, `department_name`, `emp_reference`, `emp_salary`) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {},  {});".format(emp_id, emp_firstname, emp_lastname, emp_DOB, emp_nid, emp_phone, emp_address, department_name, emp_reference, emp_salary)
        cur = self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()


    # =================== add advance salary function =====================
    def add_advance_salary(self, month, year, amount, emp_id, new_emp):
        adv_query = "INSERT INTO `advance salary` (`Month`, `Year`, `Amount`, `Employee ID`) VALUES ('{}', {}, {}, {});".format(month, year, amount, emp_id)
        cur = self.mydb.cursor() 
        cur.execute(adv_query)
        self.mydb.commit()
        if new_emp == 0:
            # date, description, money, crDr, tableName 
            des = str(month+" month, Advance salary employee id no :"+str(emp_id))
            self.table_data_entry('date', des, amount, 'D', '')
            # query = "INSERT INTO `Dailay Account`(`Date`, `Description`, Cost, cr_dr) VALUES (NOW(), '{}', {}, '{}');".format(month+" month, Advance salary employee id no :"+str(emp_id), amount, "D")
            # cur.execute(query)
            # self.mydb.commit()


    # =================== add due salary function =====================
    def add_due_salary(self, month, year, amount, emp_id):
        adv_query = "INSERT INTO `due salary` (`Month`, `Year`, `Amount`, `Employee ID`) VALUES ('{}', {}, {}, {});".format(month, year, amount, emp_id)
        cur = self.mydb.cursor() 
        cur.execute(adv_query)
        self.mydb.commit()


    # =================== add blance function =====================
    def fatch_employee_id(self):
        query = "SELECT `emp_id` FROM `employees`;"
        cur = self.mydb.cursor()
        cur.execute(query)
        emp_id = []
        for i in cur:
            emp_id.append(i[0])
        return emp_id




    # =================== add blance function =====================

    def add_blance(self, date, money):
        cur = self.mydb.cursor()
        query = "INSERT INTO `Dailay Account`(`Date`, `Description`, blance , cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, 'B/F', money, 'B')
        cur.execute(query)
        self.mydb.commit()

    # =================== add blance function =====================
    def check_blance(self):
        cur = self.mydb.cursor()
        query = "SELECT blance FROM `Dailay Account` ORDER BY Id DESC LIMIT 1"
        cur.execute(query)
        for i in cur:
            return i[0]



    # =================== add table data fatch =====================
    def add_table_data_fetch(self, t_name, cd):
        cur = self.mydb.cursor()  
        if cd == 'C':
            query = "SELECT `Date`, Description, Ricived FROM `{}` WHERE cr_dr = 'C';".format(t_name)
        elif cd == 'D':
            query = "SELECT `Date`, Description, Cost FROM `{}` WHERE cr_dr = 'D';".format(t_name)
        cur.execute(query)
        all_data=cur.fetchall()
        return all_data 


    # =================== debit or credit page  search data etch =====================
    def search_table_fetch(self, t_name, cd, date):
        cur = self.mydb.cursor()  
        if cd == 'C':
            query = "SELECT `Date`, Description, Ricived FROM `{}` WHERE cr_dr = 'C' and `Date` = '{}';".format(t_name, date)
        elif cd == 'D':
            query = "SELECT `Date`, Description, Cost FROM `{}` WHERE cr_dr = 'D' and `Date` = '{}';".format(t_name, date)
        cur.execute(query)
        all_data=cur.fetchall()
        return all_data 


    # =================== debit or credit page  total amount =====================
    def search_data_total_amount(self, t_name, date, cd):
        cur = self.mydb.cursor()  
        if cd == 'C':
            if date == "All Data":
                total_query = "SELECT SUM(Ricived) FROM `{}` WHERE cr_dr = 'C';".format(t_name)
            else:
                total_query = "SELECT SUM(Ricived) FROM `{}` WHERE cr_dr = 'C' and `Date` = '{}';".format(t_name, date)
        if cd == 'D':
            if date == "All Data":
                total_query = "SELECT SUM(Cost) FROM `{}` WHERE cr_dr = 'D';".format(t_name)
            else:
                total_query = "SELECT SUM(Cost) FROM `{}` WHERE cr_dr = 'D' and `Date` = '{}';".format(t_name, date)
        cur.execute(total_query)
        total=cur.fetchall()
        return total[0][0] 


    # =================== Date To Date Search total amount =====================
    def search_dataToDate_total_amount(self, t_name, date, toDate, cd):
        cur = self.mydb.cursor()  
        if cd == 'C':
            if date == "All":
                total_query = "SELECT SUM(Ricived) FROM `{}`;".format(t_name)
            else:
                total_query = "SELECT SUM(Ricived) FROM `{}` where `date` >= '{}' and `date` <= '{}';".format(t_name, date, toDate)
        elif cd == 'D':
            if date == "All":
                total_query = "SELECT SUM(Cost) FROM `{}`;".format(t_name)
            else:
                total_query = "SELECT SUM(Cost) FROM `{}` where `date` >= '{}' and `date` <= '{}';".format(t_name, date, toDate)   
        elif cd == 'CD':
            if date == "All":
                total_query = "SELECT SUM(Ricived), SUM(Cost) FROM `{}`;".format(t_name)
            else:
                total_query = "SELECT SUM(Ricived), SUM(Cost) FROM `{}` where `date` >= '{}' and `date` <= '{}';".format(t_name, date, toDate)   
        cur.execute(total_query)
        total=cur.fetchall()
        return total

    # =================== debit or credit page search data all data etch =====================
    def search_table_all_data_fetch(self, t_name, cd):
        cur = self.mydb.cursor()  
        if cd == 'C':
            query = "SELECT `Date`, Description, Ricived FROM `{}` WHERE cr_dr = 'C' ;".format(t_name)
        elif cd == 'D':
            query = "SELECT `Date`, Description, Cost FROM `{}` WHERE cr_dr = 'D' ;".format(t_name)
        cur.execute(query)
        all_data=cur.fetchall()
        return all_data 
       
    # =================== search date to date data fetch =====================
    def search_dateToDate_data_fetch(self, t_name, date, toDate ,cd):
        cur = self.mydb.cursor()  
        if cd == 'C':
            query = "SELECT `Date`, Description, Ricived FROM `{}` where `date` >= '{}' and `date` <= '{}';".format(t_name, date, toDate)
        elif cd == 'D':
            query = "SELECT `Date`, Description, Cost FROM `{}`  where `date` >= '{}' and `date` <= '{}';".format(t_name, date, toDate)
        elif cd == 'CD':
            query = "SELECT `Date`, Description, Ricived, Cost FROM `{}`  where `date` >= '{}' and `date` <= '{}';".format(t_name, date, toDate)
        cur.execute(query)
        fetch_date=cur.fetchall()
        return fetch_date 
       
    # =================== search data all data fetch =====================
    def search_table_data_fetch(self, t_name, cd):
        cur = self.mydb.cursor()  
        if cd == 'C':
            query = "SELECT `Date`, Description, Ricived FROM `{}`;".format(t_name)
        elif cd == 'D':
            query = "SELECT `Date`, Description, Cost FROM `{}`;".format(t_name)
        elif cd == 'CD':
            query = "SELECT `Date`, Description, Ricived, Cost FROM `{}`;".format(t_name)
        cur.execute(query)
        all_data=cur.fetchall()
        return all_data 
       
    # =================== add department table =====================
    def add_department(self, dep_name):
            query = "INSERT INTO `department` (`department_name`) VALUES ('{}');".format(dep_name)
            cur = self.mydb.cursor()  
            cur.execute(query)
            self.mydb.commit()

    # =================== add department table =====================
    def fatch_department_name(self):
        cur = self.mydb.cursor()  
        query = "SELECT `department_name`FROM `department`;"
        cur.execute(query)
        names=cur.fetchall()
        names_list = []
        for i in names:
            names_list.append(i[0])
        return names_list

    # =================== employee name and salary =====================
    def fatch_name_employees(self, emp_id):
        cur = self.mydb.cursor()  
        query = "SELECT emp_firstname,  emp_lastname, emp_salary FROM employees where emp_id = {};".format(emp_id)
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            return i

    # =================== employee advance salary =====================
    def fatch_adv_net_sel(self, emp_id, month):
        print(month)
        cur = self.mydb.cursor()  
        query = "SELECT sum(`Amount`) FROM `advance salary` where `month` = '{}' and `Year` = year(now()) and `Employee ID` = {};".format(month, emp_id)
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            return i[0]
    # =================== employee previous month salary =====================
    def previous_month_sal(self, emp_id, month):
        month_all = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        mon_index = month_all.index(month)
        cur = self.mydb.cursor()  
        if mon_index == 0:
            query = "SELECT Amount FROM `due salary` where `Month` = '{}' and `Year` = (year(now())-1) and `Employee ID` = {};".format(month_all[mon_index-1], emp_id)
        else:
            query = "SELECT Amount FROM `due salary` where `Month` = '{}' and `Year` = year(now()) and `Employee ID` = {};".format(month_all[mon_index-1], emp_id)
        cur.execute(query)
        result=cur.fetchall()
        for i in result:
            return i[0]


    # =================== employee due salary =====================
    def add_salary_date(self,  emp_id, name, work, attaen, month, advance, due, net_salary, pay_amount):
        cur = self.mydb.cursor()  
        query = "INSERT INTO `salary` (`emp_id`, `emp Name`, `working day`, `attendance day`, `month`, `net advance salary`, `net due salary`, `net salary`, `payment salary`) VALUES ({}, '{}', {}, {}, '{}', {}, {}, {}, {});".format( emp_id, name, work, attaen, month, advance, due, net_salary, pay_amount)
        cur.execute(query)
        self.mydb.commit()
        des = str(month+" month, Advance salary employee id no :"+str(emp_id))
        self.table_data_entry('date', des, net_salary, 'D', '')
        if (net_salary - pay_amount) > 0:
            due_query = "INSERT INTO `due salary` (`Month`, `Year`, `Amount`, `Employee ID`) VALUES ('{}', year(now()), {}, {});".format(month, (net_salary - pay_amount), emp_id)
            cur = self.mydb.cursor() 
            cur.execute(due_query)
            self.mydb.commit()
        elif (net_salary - pay_amount) < 0:
            month_all = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            mon_index = month_all.index(month)
            if mon_index == 11:
                adv_query = "INSERT INTO `advance salary` (`Month`, `Year`, `Amount`, `Employee ID`) VALUES ('{}', (year(now())+1), {}, {});".format(month_all[0], ((-1)*(net_salary - pay_amount)), emp_id)
                des = str(month_all[0]+" month, Advance salary employee id no :"+str(emp_id))
                self.table_data_entry('date', des, ((-1)*(net_salary - pay_amount)), 'D', '')
            else:
                adv_query = "INSERT INTO `advance salary` (`Month`, `Year`, `Amount`, `Employee ID`) VALUES ('{}', (year(now())), {}, {});".format(month_all[mon_index+1], ((-1)*(net_salary - pay_amount)), emp_id)
                des = str(month_all[mon_index+1]+" month, Advance salary employee id no :"+str(emp_id))
                self.table_data_entry('date', des, ((-1)*(net_salary - pay_amount)), 'D', '')
            cur = self.mydb.cursor() 
            cur.execute(adv_query)
            self.mydb.commit()

    # =================== employee promotion =====================
    def employee_promotion(self, dep, salary, id):
        query = "UPDATE `employees` SET `department_name` = '{}', `emp_salary` = '{}' WHERE (`emp_id` = '{}');".format(dep, salary, id)
        cur = self.mydb.cursor() 
        cur.execute(query)
        self.mydb.commit()

    # =================== employee search =====================
    def search_employee(self, id):
        if id == "All":
            query = "SELECT emp_id, emp_firstname, emp_lastname, emp_DOB, emp_nid, emp_phone, emp_address, department_name, emp_reference, date(emp_join_date), emp_salary  FROM employees ;"
        else:
            query = "SELECT emp_id, emp_firstname, emp_lastname, emp_DOB, emp_nid, emp_phone, emp_address, department_name, emp_reference, date(emp_join_date), emp_salary  FROM employees where emp_id = {};".format(id)
        cur = self.mydb.cursor() 
        cur.execute(query)
        result=cur.fetchall()
        imp_list = []
        for i in result:
            imp_list.append(i)
        return imp_list 



# parson = Mydatabase()
# parson.add_blance('2022-04-25', 5584)
# parson.table_data_entry('2022-04-25', "PRINTING & STATION: OFFI: MR. MUNNA RECEV: OFFI: WEBSIDE PUR: ", 5000, 'D', 'Cash Receiv/Pay' )
# parson.table_data_entry('2022-04-25', "CASH REVEV: FROM MD. FOR OFFICIAL COSTING PUR: BY MR. BABU", 50000, 'C', 'Cash Receiv/Pay' )
# parson.table_data_entry('2022-04-25', "CASH RECEV: FROM JANATA BANK FOR OFFICE COSTING PUR: BY BAPPY", 50000, 'C', 'Cash Receiv/Pay' )
# parson.table_data_entry('2022-04-25', "PRINTING & STATION: OFFI: MR. MUNNA RECEV: FOR HARD DISK, INK ETC", 2660, 'D', 'Stationary' )
# parson.table_data_entry('2022-04-25', "MAINTENAN: OFFI: SHAMIM RECEV: FOR OFFI: 4TH FLOOR’S LIGHT SET UP ", 1100, 'D', 'Office Maintenance' )
# parson.table_data_entry('2022-04-26', "ENTERTAIN: OFFI: MIRAZ RECEV: FOR MD’S PUR: 1 CARTON CIGARETTE", 3000, 'D', 'Dailay Expendeture' )
# parson.table_data_entry('2022-04-26', "CONVEY: OFFI: MR. BABU RECEV: FOR OFFICE PUR: ZIGATALA, SAVAR", 200, 'D', 'Convance' )
# parson.table_data_entry('2022-04-26', "TNT BILL (OFFI:) MR. IMRAN RECEV: FOR OFFICE TNT PUR: TAR SETTING", 550, 'D', 'TNT/Mobile Bill Office' )
# parson.table_data_entry('2022-04-26', "POSTAGE & COURI: SERVI: TARIKUL (FEDEX) RECEV: FOR LEA: SAMPLE", 5500, 'D', 'Courier' )
# parson.table_data_entry('2022-04-26', "GIFT: SPL TNY MR. RUBEL (RELIANCE TNY) RECEV: BY MR. BABU", 20000, 'D', 'Gift' )
# parson.table_data_entry('2022-04-26', "MAINTENAN: RESIDEN: TAHMEED RECEV: FOR MD’S HOUSE PUR: COST", 2000, 'D', 'MD Houae' )
# parson.table_data_entry('2022-04-26', "MAINTENAN: RESIDEN: TAHMEED RECEV: FOR MD’S HOUSE PUR: COST", 5000, 'D', 'MD Houae Baribadh' )
# parson.table_data_entry('2022-04-26', "PURCHASED OF MD’S LARGE CAR PUR: NEW EQUIPMENTS & REPAIRING", 50000, 'D', 'MD Car' )
# parson.table_data_entry('2022-04-26', "MOBILE BILL (MD’S) MR. BABU RECEV: FOR MD’S MOBILE PUR: (B – KASH) ", 5000, 'D', 'MD Mobil & BKash' )
# parson.table_data_entry('2022-04-26', "CREDIT CARD (MD’S) MR. BABU RECEV: FOR MD’S CARD PUR: BANK ASIA", 5000, 'D', 'MD Credit Card Payment' )
# parson.table_data_entry('2022-04-26', "CASH RECEV: FROM MD. FOR OFFICE COSTING PUR: BY MR. BABU", 1086000, 'C', 'Managing Director' )
# parson.table_data_entry('2022-04-26', "LOAN TO MD. BY MR. BABU", 1000, 'D', 'Managing Director' )
# parson.table_data_entry('2022-04-26', "FEES & TAX MR. BAPPY (DRIVER) RECEV: FOR MD’S CAR TAX & FITNESS", 5000, 'D', 'Fees & Tex' )
# parson.table_data_entry('2022-04-26', "C & F CHARGE LITON RECEV: FOR (DUTY) COST OF P.O. (KE/KELVIN– 01/22)", 5500, 'D', 'C & F' )
# parson.fatch_table_name("C")





# SELECT DATE_ADD('2022-05-15', INTERVAL 1 DAY);
# select  *
# from `dailay account`
# where `date` >= '2022-05-14' and `date` <= '2022-05-14';    
