# Mini Project
import pymysql
from prettytable import from_db_cursor
import hashlib

# --------------------------------------------------------------------------------Load tables-------------------------------------------------------------------#
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "password"
MYSQL_DB = "test"

# Establish a database connection
connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
cursor = connection.cursor()


# --------------------------------------------------------------------------------Define the functions-------------------------------------------------------------------#
# Main Menu Functions
def exit_func():
    # --------------------------------------------------------------------Saving data to order_menu.csv---------------------------------------------------------------#
    while True:
        print("""
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
         |🛒 You have logged out The Order Management System 🛒|
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
        """)
        return False



def call_main_menu():
    main_menu_option = int(input(
        """
     +-+-+ +-+-+-+-+-+-+-+ 
     |1|  Product   Menu |
     +-+-+ +-+-+-+-+-+-+-+ 
     |2|  Courier   Menu |
     +-+-+ +-+-+-+-+-+-+-+
     |3|  Order     Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     |4|  Search    Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     |0|       EXIT      |    
     +-+-+ +-+-+-+-+-+ +-+
     """))

    if main_menu_option == 1:
        call_product_menu()

    elif main_menu_option == 2:
        call_courier_menu() 
 
    elif main_menu_option == 3:
        call_order_menu()

    elif main_menu_option == 4:
        call_search_menu()

    elif main_menu_option == 0:
        exit_func()
        return False


# Products functions
def print_product_list():
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)


def create_new_product():
    # To create a new order
    product_cursor = connection.cursor()
    new_product_id = input("New product id: ")
    new_product_name = input("New product name: ")
    new_product_price = input("New product price: £")

    try:
        cpro_sql = "INSERT INTO products (product_id, name, price) VALUES (%s, %s, %s)"
        cpro_val = (f'{new_product_id}',f'{new_product_name}', f'{new_product_price}')
        product_cursor.execute(cpro_sql, cpro_val)
    except Exception as e:
        pass

    connection.commit()
    # To print the updated products menu
    
    print("Updated Products menu:")
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)


def update_existing_product():
    product_cursor = connection.cursor()
    connection.commit()
    print("Updated Products menu:")
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)

    try:
        update_product_index = int(input("Product index: "))
    except Exception as e:
        pass
    update_product_name = input("Update product name: ")
    update_product_price = input("Update product price: £")

    try:
        u_sql = "UPDATE products SET name = %s, price = %s WHERE product_id = %s"
        u_val = (f'{update_product_name}', f'{update_product_price}', f'{update_product_index}')
        product_cursor.execute(u_sql, u_val)
    except Exception as e:
        pass

    # To print the updated products menu
    product_cursor.execute('SELECT * FROM products')
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)

def delete_product():
    product_cursor = connection.cursor()
    print("Updated Products menu:")
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)
    connection.commit()
    try:
        delete_product_index = int(input("Delete Product Index: "))
    except Exception as e:
        pass

    try:
        d_sql = "DELETE FROM products WHERE product_id = %s ;"
        d_val = f'{delete_product_index}'
        product_cursor.execute(d_sql, d_val)
    except Exception as e:
        pass
    
    connection.commit()

    # To print the updated products menu
    
    print("Updated Products menu:")
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)



# Order functions
def print_order():
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)

def create_order():
    new_order_id = input("New order id: ")
    new_customer_name = input("New customer's name: ").capitalize()
    new_customer_address = input("New customer's address: ").capitalize()
    new_customer_phone = input("New customer's phone number: ")

    # Print Product menu
    product_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)

    new_customer_items = str(input("Purchased products | Please input the Product id: "))

    # Print courier menu
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)

    new_customer_courier = int(input("Courier's name | Please input the Courier ID:"))
    new_order_status = 1

    order_cursor = connection.cursor()

    try: 
        co_sql = "INSERT INTO orders (order_id, customer_name, customer_address, customer_phone, courier_id, status_id, product_id) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        co_val = (f'{new_order_id}', f'{new_customer_name}', f'{new_customer_address}', f'{new_customer_phone}', f'{new_customer_courier}', f'{new_order_status}', f'{new_customer_items}')
        order_cursor.execute(co_sql, co_val)
    except Exception as e:
        pass

    # Print the order menu
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)
    

def update_existing_status():
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)

    try:
        update_order_id = int(input(f"Update Order ID: "))
    except Exception as e:
        pass


    # print status
    status_cursor = connection.cursor()
    status_cursor.execute('SELECT * FROM OrderStatus')
    rows = status_cursor.fetchall()
    print("Order status:")
    for row in rows:
        print(f'Status ID: {str(row[0])}, Status: {row[1]}')
    connection.commit()

    try:
        update_status = int(input(f"New order status ID: "))
    except Exception as e:
        pass
    
    try:
        us_sql = "UPDATE orders SET status_id = %s WHERE order_id = %s"
        us_val = (f'{update_status}', f'{update_order_id}')
        order_cursor.execute(us_sql, us_val)
    except Exception as e:
        pass

    # To print the updated products menu
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)


def update_existing_order():
    # Print the order table
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)

    try:
        update_order_id = int(input("Update Order ID: "))
    except Exception as e:
        pass
    update_customer_name = input("New customer Name: ")
    update_customer_address = input("New customer Address: ")
    update_customer_phone = input("New customer phone number: ")

    # print courier table
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)

    try:
        update_courier_id = int(input("New courier ID: "))
    except Exception as e:
        pass

    # print product table
    product_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)

    new_customer_items = str(input("Purchased products | Please input the Product id: "))

    order_cursor = connection.cursor()

    try:
        co_sql = "UPDATE orders SET customer_name= %s, customer_address= %s, customer_phone= %s, courier_id= %s, product_id= %s  WHERE order_id = %s"
        co_val = (f'{update_customer_name}', f'{update_customer_address}', f'{update_customer_phone}', f'{update_courier_id}', f'{new_customer_items}', f'{update_order_id}')
        order_cursor.execute(co_sql, co_val)
    except Exception as e:
        pass

    # Print the order menu
    order_cursor.execute('SELECT * FROM orders')
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)


def delete_order():
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)

    try:
        delete_order_index = input("Delete Order ID: ")
    except Exception as e:
        pass

    try:
        do_sql = "DELETE FROM orders WHERE order_id = %s ;"
        do_val = f'{delete_order_index}'
    except Exception as e:
        pass

    order_cursor.execute(do_sql, do_val)

    # To print the updated order menu
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)


# Courier functions
def print_courier():
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)


def create_courier():
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)

    # To create a new order
    courier_cursor = connection.cursor()
    new_courier_name = input("New Courier Name: ")
    new_courier_phone = input("New Courier Phone Number: ")

    try:
        cc_sql = "INSERT INTO couriers (name, phone_number) VALUES (%s, %s)"
        cc_val = (f'{new_courier_name}', f'{new_courier_phone}')
        courier_cursor.execute(cc_sql, cc_val)
    except Exception as e:
        pass

    # To print the updated COURIER menu
    courier_cursor.execute('SELECT * FROM couriers')
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)



def update_courier():
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)


    try:
        update_courier_index = int(input("Courier Index: "))
    except Exception as e:
        pass
    update_courier_name = input("Update Courier Name: ")
    update_courier_phone = input("Update Courier Phone Number: 📞")

    try:
        cu_sql = "UPDATE couriers SET name = %s, phone_number = %s WHERE courier_id = %s"
        cu_val = (f'{update_courier_name}', f'{update_courier_phone}', f'{update_courier_index}')
        courier_cursor.execute(cu_sql, cu_val)
    except Exception as e:
        pass

    # To print the updated courier menu
    courier_cursor.execute('SELECT * FROM couriers')
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)



def delete_courier():
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)

    
    delete_courier_index = int(input("Delete Courier Index: "))
    
    try:
        cd_sql = "DELETE FROM couriers WHERE courier_id = %s ;"
        cd_val = f'{delete_courier_index}'
        courier_cursor.execute(cd_sql, cd_val)
    except Exception as e:
        pass

    # To print the updated courier menu
    courier_cursor.execute('SELECT * FROM couriers')
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)

def search_by_courier():
    # print couriers_table
    courier_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM couriers")
    courier_table = from_db_cursor(cursor)
    print(courier_table)
    
    try:
        s_courier_id = int(input("Search by courier ID: "))
    except Exception as e:
        print('Wrong input!')
        pass

    order_cursor = connection.cursor()

    try:
        s_sql = "SELECT * FROM orders WHERE courier_id = %s ;"
        s_val = f'{s_courier_id}'
        order_cursor.execute(s_sql, s_val)
    except Exception as e:
        pass


    print(f"Orders under Courier ID {s_courier_id}:")
    connection.commit()
    order_table = from_db_cursor(order_cursor)
    print(order_table)
    

def search_by_product():
    # print products_table
    product_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM products")
    product_table = from_db_cursor(cursor)
    print(product_table)

    try:
        s_product_id = str(input("Search by Product ID: "))
    except Exception as e:
        print("Wrong input!")
        pass

    order_cursor = connection.cursor()


    sp_sql = f"SELECT * FROM orders WHERE product_id LIKE ('%{s_product_id}%');"
    order_cursor.execute(sp_sql)
    

    print(f"Orders under Product ID {s_product_id}:")
    connection.commit()
    order_table = from_db_cursor(order_cursor)
    print(order_table)

def search_by_order():
    # print orders_table
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM orders")
    order_table = from_db_cursor(cursor)
    print(order_table)

    try:
        s_order_id = str(input("Search by Order ID: "))
    except Exception as e:
        print("Wrong input!")
        pass

    order_cursor = connection.cursor()

    try:
        so_sql = "SELECT * FROM orders WHERE order_id = %s ;"
        so_val = f'{s_order_id}'
        order_cursor.execute(so_sql, so_val)
    except Exception as e:
        pass

    print(f"Orders under Order ID {s_order_id}:")
    connection.commit()
    order_table = from_db_cursor(order_cursor)
    print(order_table)

def search_by_status():
    # print orders_table
    order_cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM OrderStatus")
    status_table = from_db_cursor(cursor)
    print(status_table)

    try:
        s_order_id = str(input("Search by Status ID: "))
    except Exception as e:
        print("Wrong input!")
        pass

    order_cursor = connection.cursor()

    try:
        so_sql = "SELECT * FROM orders WHERE status_id = %s ;"
        so_val = f'{s_order_id}'
        order_cursor.execute(so_sql, so_val)
    except Exception as e:
        pass

    print(f"Orders under Status ID {s_order_id}:")
    connection.commit()
    order_table = from_db_cursor(order_cursor)
    print(order_table)

def call_product_menu():
    customer_product_order = int(input(
            """
     +-+-+ +-+-+-+-+-+-+-+ 
     |1|  View      Menu |
     +-+-+ +-+-+-+-+-+-+-+ 
     |2|  Create Product |
     +-+-+ +-+-+-+-+-+-+-+
     |3|  Update Product |    
     +-+-+ +-+-+-+-+-+ +-+
     |4|  Delete  Product|    
     +-+-+ +-+-+-+-+-+ +-+
     |0|  MAIN      Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     """))
    if customer_product_order == 0:
        call_main_menu()

    elif customer_product_order == 1:
        print_product_list()
        call_product_menu()

    elif customer_product_order == 2:
        create_new_product()
        call_product_menu()

    elif customer_product_order == 3:
        update_existing_product()
        call_product_menu()

    elif customer_product_order == 4:
        delete_product()
        call_product_menu()

    else:
        print("Your information is wrong.")
        call_product_menu()

def call_courier_menu():
    courier_detail = int(input(
            """
     +-+-+ +-+-+-+-+-+-+-+ 
     |1|  View      Menu |
     +-+-+ +-+-+-+-+-+-+-+ 
     |2|  Create Courier |
     +-+-+ +-+-+-+-+-+-+-+
     |3|  Update Courier |    
     +-+-+ +-+-+-+-+-+ +-+
     |4|  Delete  Courier|    
     +-+-+ +-+-+-+-+-+ +-+
     |0|  Main      Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     """))
    if courier_detail == 0:
        call_main_menu()

    elif courier_detail == 1:
        print_courier()
        call_courier_menu()

    elif courier_detail == 2:
        create_courier()
        call_courier_menu()

    elif courier_detail == 3:
        update_courier()
        call_courier_menu()

    elif courier_detail == 4:
        delete_courier()
        call_courier_menu()
    else:
        print("Your information is wrong.")
        call_main_menu()

def call_order_menu():
    customer_detail_order = int(input(
            """
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     |1|  View           Menu |
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     |2|  Create        Order |
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     |3|  Update Order Status |    
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     |4|  Update        Order |  
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     |5|  Delete        Order |   
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     |0|  MAIN           Menu |    
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     """))
    if customer_detail_order == 0:
        call_main_menu()

    elif customer_detail_order == 1:
        print_order()
        call_order_menu()

    elif customer_detail_order == 2:
        create_order()
        call_order_menu()

    elif customer_detail_order == 3:
        update_existing_status()
        call_order_menu()

    elif customer_detail_order == 4:
        update_existing_order()
        call_order_menu()

    elif customer_detail_order == 5:
        delete_order()
        call_order_menu()

    else:
        print("Your information is wrong.")
        call_main_menu()

def call_search_menu():
    s_cat = int(input("""
     +-+-+-+-+-+-+-+-+-
     |    Search By   |
     +-+-+-+-+-+-+-+-+-
     |1|  Courier ID  |
     +-+-+-+-+-+-+-+-+-
     |2|  Product ID  |    
     +-+-+-+-+-+-+-+-+-
     |3|  Order   ID  |    
     +-+-+-+-+-+-+-+-+-
     |4|  Status  ID  |    
     +-+-+-+-+-+-+-+-+-
     |0|  MAIN   Menu |    
     +-+-+-+-+-+-+-+-+-
     """))
    if s_cat == 1:
        search_by_courier()
        call_search_menu()
        
    elif s_cat == 2:
        search_by_product()
        call_search_menu()
        
    elif s_cat == 3:
        search_by_order()
        call_search_menu()
        
    elif s_cat == 4:
        search_by_status()
        call_search_menu()
    
    elif s_cat == 0:
        call_main_menu()

    else:
        print("Your input is wrong.")
        call_main_menu()
# ----------------------------------------------------------Start here--------------------------------------------------------------------------------------------#
print("""
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
 |🛒 Welcome To The Order Management System of Pop Up Cafe 🛒|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
""")

def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open(r"D:\4. bootcamp\mini_project\vsc\credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")


def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open(r"D:\4. bootcamp\mini_project\vsc\credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()

    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in Successfully!")
        while True:
            call_main_menu()
            break
    else:
        print("Login failed! \n")


while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Confirm EXIT")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")