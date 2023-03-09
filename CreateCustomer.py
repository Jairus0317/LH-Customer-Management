import sqlite3

connection = sqlite3.connect("LH_Database.db")

cursor = connection.cursor()


command_create_table = "CREATE TABLE IF NOT EXISTS customers(name TEXT, plate TEXT, deposit REAL, loanterm INTEGER, monthly REAL, vehicle TEXT, engineno TEXT, bookno INTEGER, bookindex INTEGER)"

cursor.execute(command_create_table)

def add_customer_function(name, plate, deposit, loanterm, monthly, vehicle, engineno, bookno, bookindex):
    print(name, plate, deposit, loanterm, monthly, vehicle, engineno, bookno, bookindex)
    cursor.execute("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?)", (name, plate, deposit, loanterm, monthly, vehicle, engineno, bookno, bookindex))

    connection.commit()




def get_all_customers():
    cursor.execute("SELECT * FROM customers")
    customers=cursor.fetchall()

    return customers



