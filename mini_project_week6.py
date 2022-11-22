# Mini Project
import pymysql
import os

# --------------------------------------------------------------------------------Load tables-------------------------------------------------------------------#
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")

# Establish a database connection
connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)

# --------------------------------------------------------------------------------Define the functions-------------------------------------------------------------------#
# Main Menu Functions
def exit_func():
    # --------------------------------------------------------------------Saving data to order_menu.csv---------------------------------------------------------------#
    while True:
        print("""
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
         |🛒 End of The Order Management System 🛒|
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
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
     |0|  EXIT      Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     """))

    if main_menu_option == 1:
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
     |0|  EXIT      Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     """))
        if customer_product_order == 0:
            call_main_menu()

        elif customer_product_order == 1:
            print_product_list()
            call_main_menu()

        elif customer_product_order == 2:
            create_new_product()
            call_main_menu()

        elif customer_product_order == 3:
            update_existing_product()
            call_main_menu()

        elif customer_product_order == 4:
            delete_product()
            call_main_menu()

        else:
            print("Your information is wrong.")
            call_main_menu()

    # ----------------------------------------------------------Courier--------------------------------------------------------------------------------------------#
    elif main_menu_option == 2:
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
     |0|  EXIT      Menu |    
     +-+-+ +-+-+-+-+-+ +-+
     """))
        if courier_detail == 0:
            call_main_menu()

        elif courier_detail == 1:
            print_courier()
            call_main_menu()

        elif courier_detail == 2:
            create_courier()
            call_main_menu()

        elif courier_detail == 3:
            update_courier()
            call_main_menu()

        elif courier_detail == 4:
            delete_courier()
            call_main_menu()
        else:
            print("Your information is wrong.")
            call_main_menu()

    # ----------------------------------------------------------Order--------------------------------------------------------------------------------------------#
    elif main_menu_option == 3:
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
     |0|  EXIT           Menu |    
     +-+-+ +-+-+-+-+-+-+-+-+-+-
     """))
        if customer_detail_order == 0:
            call_main_menu()

        elif customer_detail_order == 1:
            print_order()
            call_main_menu()

        elif customer_detail_order == 2:
            create_order()
            call_main_menu()

        elif customer_detail_order == 3:
            update_existing_status()
            call_main_menu()

        elif customer_detail_order == 4:
            update_existing_order()
            call_main_menu()

        elif customer_detail_order == 5:
            delete_order()
            call_main_menu()

        else:
            print("Your information is wrong.")
            call_main_menu()

    elif main_menu_option == 4:
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
     |0|  EXIT   Menu |    
     +-+-+-+-+-+-+-+-+-
     """))
        if s_cat == 1:
            search_by_courier()
            call_main_menu()
        
        elif s_cat == 2:
            search_by_product()
            call_main_menu()
        
        elif s_cat == 3:
            search_by_order()
            call_main_menu()

        else:
            print("Your input is wrong.")
            call_main_menu()
    

    elif main_menu_option == 0:
        exit_func()
        return False


# Products functions
def print_product_list():
    product_cursor = connection.cursor()
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()


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

    # To print the updated products menu
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Updated Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()


def update_existing_product():
    product_cursor = connection.cursor()
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Updated Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()

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
    rows = product_cursor.fetchall()
    print("Updated Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()


def delete_product():
    product_cursor = connection.cursor()
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Updated Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
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

    # To print the updated products menu
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Updated Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()


# Order functions
def print_order():
    order_cursor = connection.cursor()
    order_cursor.execute('SELECT * FROM orders ORDER BY order_id;')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

def create_order():
    new_order_id = input("New order id: ")
    new_customer_name = input("New customer's name: ").capitalize()
    new_customer_address = input("New customer's address: ").capitalize()
    new_customer_phone = input("New customer's phone number: ")

    # Print Product menu
    product_cursor = connection.cursor()
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()

    new_customer_items = str(input("Purchased products | Please input the Product id: "))

    # Print courier menu
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    cou_rows = courier_cursor.fetchall()
    print("Couriers menu:")
    for row in cou_rows:
        print(f'id: {str(row[0])}, name: {row[1]}, 📞phone: {row[2]}')

    connection.commit()

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
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()
    

def update_existing_status():
    order_cursor = connection.cursor()
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

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
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()


def update_existing_order():
    # Print the order table
    order_cursor = connection.cursor()
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

    try:
        update_order_id = int(input("Update Order ID: "))
    except Exception as e:
        pass
    update_customer_name = input("New customer Name: ")
    update_customer_address = input("New customer Address: ")
    update_customer_phone = input("New customer phone number: ")

    # print courier table
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Couriers menu:")
    for row in rows:
        print(f'id: {str(row[0])}, name: {row[1]}, 📞phone: {row[2]}')

    connection.commit()

    try:
        update_courier_id = int(input("New courier ID: "))
    except Exception as e:
        pass

    # print product table
    product_cursor = connection.cursor()
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()

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
    rows = order_cursor.fetchall()
    print("Updated Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()


def delete_order():
    order_cursor = connection.cursor()
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

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
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()


# Courier functions
def print_courier():
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Couriers menu:")
    for row in rows:
        print(f'id: {str(row[0])}, name: {row[1]}, 📞phone: {row[2]}')

    connection.commit()


def create_courier():
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    for row in rows:
        print(f'id: {str(row[0])}, Courier name: {row[1]}, 📞Phone number: {row[2]}')

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

    # To print the updated products menu
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Updated Courier menu:")
    for row in rows:
        print(f'id: {str(row[0])}, Courier name: {row[1]}, 📞Phone number: {row[2]}')
    connection.commit()


def update_courier():
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Courier menu:")
    for row in rows:
        print(f'id: {str(row[0])}, Courier name: {row[1]}, 📞Phone number: {row[2]}')
    connection.commit()

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

    # To print the updated products menu
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Updated Courier menu:")
    for row in rows:
        print(f'id: {str(row[0])}, Courier name: {row[1]}, 📞Phone number: {row[2]}')
    connection.commit()


def delete_courier():
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Courier menu:")
    for row in rows:
        print(f'id: {str(row[0])}, Courier name: {row[1]}, 📞Phone number: {row[2]}')
    connection.commit()
    delete_courier_index = int(input("Delete Courier Index: "))
    
    try:
        cd_sql = "DELETE FROM couriers WHERE courier_id = %s ;"
        cd_val = f'{delete_courier_index}'
        courier_cursor.execute(cd_sql, cd_val)
    except Exception as e:
        pass

    # To print the updated products menu
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Updated Courier menu:")
    for row in rows:
        print(f'id: {str(row[0])}, Courier name: {row[1]}, 📞Phone number: {row[2]}')
    connection.commit()

def search_by_courier():
    # print couriers_table
    courier_cursor = connection.cursor()
    courier_cursor.execute('SELECT * FROM couriers')
    rows = courier_cursor.fetchall()
    print("Couriers menu:")
    for row in rows:
        print(f'id: {str(row[0])}, name: {row[1]}, 📞phone: {row[2]}')
    connection.commit()
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

    rows = order_cursor.fetchall()
    print(f"Orders under Courier ID {s_courier_id}:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

def search_by_product():
    # print products_table
    product_cursor = connection.cursor()
    product_cursor.execute('SELECT * FROM products')
    rows = product_cursor.fetchall()
    print("Products menu:")
    for row in rows:
        print(f'id: {str(row[0])}, product name: {row[1]}, price: £{row[2]}')
    connection.commit()

    try:
        s_product_id = str(input("Search by Product ID: "))
    except Exception as e:
        print("Wrong input!")
        pass

    order_cursor = connection.cursor()


    sp_sql = f"SELECT * FROM orders WHERE product_id LIKE ('%{s_product_id}%');"
    order_cursor.execute(sp_sql)
    

    rows = order_cursor.fetchall()
    print(f"Orders under Product ID {s_product_id}:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

def search_by_order():
    # print orders_table
    order_cursor = connection.cursor()
    order_cursor.execute('SELECT * FROM orders')
    rows = order_cursor.fetchall()
    print("Order menu:")
    for row in rows:
        print(
            f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()

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

    rows = order_cursor.fetchall()
    print(f"Orders under Order ID {s_order_id}:")
    for row in rows:
        print(f'Order ID: {str(row[0])}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone Number: {row[3]}, Courier ID: {row[4]}, Order Status ID: {row[5]}, Items: {row[6]}')
    connection.commit()


# ----------------------------------------------------------Start here--------------------------------------------------------------------------------------------#
print("""
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
 |🛒 Welcome To The Order Management System of Pop Up Cafe 🛒|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
""")

while True:
    call_main_menu()
    break