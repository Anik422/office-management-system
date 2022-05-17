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
        create_dailay_account = "CREATE TABLE if not exists `Dailay Account`(Id int NOT NULL AUTO_INCREMENT , `Date`  DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int DEFAULT 0, Cost int DEFAULT 0, Blance int DEFAULT 0, cr_dr varchar(1) NOT NULL, PRIMARY KEY(Id));"
        cur.execute(create_dailay_account)
        create_Cash_Receiv_Pay = "CREATE TABLE if not exists `Cash Receiv/Pay` ( Id int AUTO_INCREMENT , `Date`  DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int DEFAULT 0, Cost int DEFAULT 0, cr_dr varchar(1) NOT NULL,  PRIMARY KEY(Id));"
        cur.execute(create_Cash_Receiv_Pay)
        create_stationary = "CREATE TABLE if not exists `Stationary` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_stationary)
        create_Office_Maintenance = "CREATE TABLE if not exists `Office Maintenance` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Office_Maintenance)
        create_Dailay_Expendeture = "CREATE TABLE if not exists `Dailay Expendeture` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Dailay_Expendeture)
        create_Convance  = "CREATE TABLE if not exists `Convance` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Convance)
        create_TNT_Mobile_Bill_Office = "CREATE TABLE if not exists `TNT/Mobile Bill Office` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_TNT_Mobile_Bill_Office )
        create_Courier = "CREATE TABLE if not exists `Courier` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Courier )
        create_Gift = "CREATE TABLE if not exists `Gift` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Gift )
        create_MD_Houae = "CREATE TABLE if not exists `MD Houae` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_MD_Houae )
        create_MD_Houae_Baribadh = "CREATE TABLE if not exists `MD Houae Baribadh` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_MD_Houae_Baribadh )
        create_MD_Car = "CREATE TABLE if not exists `MD Car` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_MD_Car)
        create_MD_Mobil_BKash = "CREATE TABLE if not exists `MD Mobil & BKash` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_MD_Mobil_BKash)
        create_MD_Credit_Card_Payment = "CREATE TABLE if not exists `MD Credit Card Payment` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_MD_Credit_Card_Payment)
        create_Managing_Director = "CREATE TABLE if not exists `Managing Director`( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Ricived int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Managing_Director)
        create_Fees_Tex = "CREATE TABLE if not exists `Fees & Tex` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Fees_Tex)
        create_C_and_F = "CREATE TABLE if not exists `C & F` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_C_and_F)
        create_Carring_Cost = "CREATE TABLE if not exists `Carring Cost` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Carring_Cost)
        create_bill = "CREATE TABLE if not exists `Bill` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_bill)
        create_rent_sever_office = "CREATE TABLE if not exists `RENT SEVER OFFICE` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_rent_sever_office)
        create_rent_head_office = "CREATE TABLE if not exists `RENT HEAD OFFICE` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_rent_head_office)
        create_Renewal_Fees = "CREATE TABLE if not exists `Renewal Fees` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Renewal_Fees)
        create_Machinaries_setup_Maintenance = "CREATE TABLE if not exists `Tannery Machinaries setup and Maintenance` ( Id int NOT NULL AUTO_INCREMENT , `Date` DATE NOT NULL, `Description` varchar(500) NOT NULL, Cost int NOT NULL, cr_dr varchar(1) NOT NULL, PRIMARY KEY (Id) );"
        cur.execute(create_Machinaries_setup_Maintenance)
        # create all table query set end


    def table_data_entry(self, date, description, money, crDr, tableName ):
        global table_query
     
        #all table data insart start
        #credit Account data insart start     
        if crDr == 'C':      
            query = "INSERT INTO `Dailay Account`(`Date`, `Description`, Ricived, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, description, money, crDr)
            if tableName == 'Cash Receiv/Pay': #Cash Receiv/Pay table debit data insert
                table_query = "INSERT INTO `Cash Receiv/Pay`(`Date`, `Description`, Ricived, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, description, money, crDr)
            elif tableName == 'Managing Director': #Cash Managing Director table debit data insert
                table_query = "INSERT INTO `Managing Director`(`Date`, `Description`, Ricived, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            cur = self.mydb.cursor()
            cur.execute(table_query)
            self.mydb.commit()
            #debit Account data insart end
        #credit Account data insart end


        #debit Account data insart start
        elif crDr == 'D':
            query = "INSERT INTO `Dailay Account`(`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, description, money, crDr)
            if tableName == 'Cash Receiv/Pay':      #Cash Receiv/Pay table credit  data insert
                table_query = "INSERT INTO `Cash Receiv/Pay`(`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format( date, description, money, crDr)
            elif tableName == 'Stationary':         #Stationary table credit  data insert
                table_query = "INSERT INTO `Stationary` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Office Maintenance':         # Office Maintenance table credit  data insert
                table_query = "INSERT INTO `Office Maintenance` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Dailay Expendeture':         # Dailay Expendeture table credit  data insert
                table_query = "INSERT INTO `Dailay Expendeture` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Convance':         # Dailay Expendeture table credit  data insert
                table_query = "INSERT INTO `Convance`(`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, {});".format(date, description, money, crDr)
            elif tableName == 'TNT/Mobile Bill Office':         # TNT/Mobile Bill Office  table credit  data insert
                table_query = "INSERT INTO `TNT/Mobile Bill Office` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Courier':         # Courier table credit  data insert
                table_query = "INSERT INTO `Courier` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Gift':         # Gift table credit data insert
                table_query = "INSERT INTO `Gift` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'MD Houae':         # MD's Houae table credit data insert
                table_query = "INSERT INTO `MD Houae` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'MD Houae Baribadh':         # MD's Houae Baribadh table credit data insert
                table_query = "INSERT INTO `MD Houae Baribadh` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'MD Car':         # MD's Car table credit data insert
                table_query = "INSERT INTO `MD Car` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'MD Mobil & BKash':         # MD's Mobil & B-Kash table credit data insert
                table_query = "INSERT INTO `MD Mobil & BKash` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'MD Credit Card Payment':         # MD's Credit Card Payment table credit data insert
                table_query = "INSERT INTO `MD Credit Card Payment` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Managing Director': # Managing Director table debit data insert
                table_query = "INSERT INTO `Managing Director`(`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr, crDr)
            elif tableName == 'Fees & Tex':         # Fees & Tex table credit data insert
                table_query = "INSERT INTO `Fees & Tex` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'C & F':         # C & F table credit data insert
                table_query = "INSERT INTO `C & F` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, {});".format(date, description, money, crDr)
            elif tableName == 'Carring Cost':         # Carring Cost table credit data insert
                table_query = "INSERT INTO `Carring Cost` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Bill':         # Bill table credit data insert
                table_query = "INSERT INTO `Bill` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'RENT SEVER OFFICE':         # RENT SEVER OFFICE table credit data insert
                table_query = "INSERT INTO `RENT SEVER OFFICE` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'RENT HEAD OFFICE':         # create_rent_head_office table credit data insert
                table_query = "INSERT INTO `RENT HEAD OFFICE` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Renewal Fees':         # Renewal Fees table credit data insert
                table_query = "INSERT INTO `Renewal Fees` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
            elif tableName == 'Tannery Machinaries setup and Maintenance':         # Renewal Fees table credit data insert
                table_query = "INSERT INTO `Tannery Machinaries setup and Maintenance` (`Date`, `Description`, Cost, cr_dr) VALUES ('{}', '{}', {}, '{}');".format(date, description, money, crDr)
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
       
    # =================== search data all data etch =====================
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
# parson.dailay_account_fetch()





# SELECT DATE_ADD('2022-05-15', INTERVAL 1 DAY);
# select  *
# from `dailay account`
# where `date` >= '2022-05-14' and `date` <= '2022-05-14';    
