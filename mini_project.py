# Mini Project
import json

product_menu_list = {"Drinks": ["Coca Cola", "Orange juice", "Milk"], "Food": ["Chicken wings", "Salad", "Sushi"]}

order_dict_list = [{
    "customer_name": "Mary",
    "customer_address": "Unit 1, 15 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887554",
    "courier": 0,
    "status": "preparing"
}, {
    "customer_name": "John",
    "customer_address": "Unit 2, 15 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887664",
    "courier": 1,
    "status": "preparing"
}, {
    "customer_name": "Susan",
    "customer_address": "Unit 3, 15 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887774",
    "courier": 2,
    "status": "preparing"
}]

order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

courier_list = ["Alice", "Betty", "Chris"]

# --------------------------------------------------------------------------------Load product_record.txt-------------------------------------------------------------------#

f = open("product_record.txt", "r")
lines = f.readlines()

for line in lines:
    print(line, end="")

# --------------------------------------------------------------------------------Load courier_record.txt-------------------------------------------------------------------#

f = open("courier_record.txt", "r")
lines = f.readlines()

for line in lines:
    print(line, end="")


# --------------------------------------------------------------------------------Define the functions-------------------------------------------------------------------#
# Main Menu Functions
def exit_func():
    print("Welcome back!")


def call_main_menu():
    int(input(
        "Please type'1'to continue the product menu, type'2' to continue the order menu, type '0' to exit the app."))


# Products functions
def print_product_list():
    print(f"We have {product_menu_list['Drinks']} in our drink menu and {product_menu_list['Food']} in our food menu.")


def print_drink_menu():
    print(f"We have {product_menu_list['Drinks']} in our drink menu.")


def print_food_menu():
    print(f"We have {product_menu_list['Food']} in our drink menu")


def create_new_product():
    new_product_category = input("Is it a drink or food?").capitalize()
    new_product = input("What product do you want to add to the menu?").capitalize()

    if new_product_category == "Drink":
        product_menu_list["Drinks"].append(new_product)
        return print_drink_menu()
    elif new_product_category == "Food":
        product_menu_list["Food"].append(new_product)
        return print_food_menu()


def update_existing_product():
    update_product_category = input("Which menu would you like to update? Drinks or food?").capitalize()

    if update_product_category == "Drinks":
        return print_drink_menu()
    elif update_product_category == "Food":
        return print_food_menu()

    update_product = input("Which product would you like to update?").capitalize()
    if update_product in product_menu_list["Drinks"]:
        return print_drink_menu()
    elif update_product in product_menu_list["Food"]:
        return print_food_menu()


def delete_product():
    delete_product_name = input("Which product would you like to delete from the menu?").capitalize()

    if delete_product_name in product_menu_list["Drinks"]:
        product_menu_list["Drinks"].remove(delete_product_name)
        return print_drink_menu()

    elif delete_product_name in product_menu_list["Food"]:
        product_menu_list["Food"].remove(delete_product_name)
        return print_food_menu()


# Order functions
def print_order():
    print(order_dict_list)


def create_order():
    new_order_name = input("Please input the customer's name.")
    new_order_address = input("Please input the customer's address.")
    new_order_phone = input("Please input the customer's phone number.")
    new_ds = {'customer_name': new_order_name, 'customer_address': new_order_address,
              'customer_phone': new_order_phone, 'status': 'preparing'}
    order_dict_list.append(new_ds)
    print(f"The updated order menu is: {order_dict_list}")
    return order_dict_list


def update_existing_status():
    index_value = ([list((i, order_dict_list[i])) for i in range(len(order_dict_list))])
    print(index_value)

    customer_update_status_index = int(input(
        "Please input the order index to update the order status of specific customer."))
    print(order_status)
    customer_update_status = input("Please update the order status.")
    order_dict_list[customer_update_status_index]["status"] = customer_update_status
    print("Your order status has been updated.")
    print(f"The updated order menu is: {order_dict_list}")
    return order_dict_list


def update_existing_order():
    index_value = ([list((i, order_dict_list[i])) for i in range(len(order_dict_list))])
    print(index_value)

    customer_update_info_check = int(
        input("Please input the order index to update the order details of specific customer."))
    for value in order_dict_list[customer_update_info_check]:
        to_be_updated_cat = input("Which information would you like to update? Name, address or phone number?").lower()
        if to_be_updated_cat == " ":
            break
        else:
            if to_be_updated_cat == "name":
                to_be_updated_name = input("Please input the new name.")
                order_dict_list[customer_update_info_check]['customer_name'] = to_be_updated_name
                print("The customer's name has been updated.")
                print(f"The updated order menu is: {order_dict_list}")
                return order_dict_list

            elif to_be_updated_cat == "address":
                to_be_updated_address = input("Please input the new address.")
                order_dict_list[customer_update_info_check]['customer_address'] = to_be_updated_address
                print("The customer's address has been updated.")
                print(f"The updated order menu is: {order_dict_list}")
                return order_dict_list

            elif to_be_updated_cat == "phone number":
                to_be_updated_phone = input("Please input the new phone number.")
                order_dict_list[customer_update_info_check]['customer_phone'] = to_be_updated_phone
                print("The customer's phone number has been updated.")
                print(f"The updated order menu is: {order_dict_list}")
                return order_dict_list


def delete_order():
    index_value = ([list((i, order_dict_list[i])) for i in range(len(order_dict_list))])
    print(index_value)

    customer_delete_index = int(
        input("Please input the order index to access the order details of specific customer."))
    order_to_be_removed = order_dict_list[customer_delete_index]
    order_dict_list.remove(order_to_be_removed)
    print("The order has been removed!")
    print(f"The updated order menu is: {order_dict_list}")
    return order_dict_list


# Courier functions
def print_courier():
    print(courier_list)


def create_courier():
    new_courier = input("Please input the name of new courier.")
    courier_list.append(new_courier)
    print(f"The updated courier list is: {courier_list}")
    return courier_list


def update_courier():
    index_value = ([list((i, courier_list[i])) for i in range(len(courier_list))])
    print(index_value)
    update_courier_index = int(input(
        "Please input the courier index to update the name of specific courier."))

    update_courier_name = input("Please input the new courier's name.")
    courier_list[update_courier_index] = update_courier_name
    print("The courier's name has been updated.")
    print(f"The updated courier list is: {courier_list}")
    return courier_list


def delete_courier():
    index_value = ([list((i, courier_list[i])) for i in range(len(courier_list))])
    print(index_value)
    delete_courier_index = int(input(
        "Please input the courier index to delete the courier."))
    courier_to_be_removed = courier_list[delete_courier_index]
    courier_list.remove(courier_to_be_removed)
    print("The courier has been removed!")
    print(f"The updated courier list is: {courier_list}")
    return courier_list


# ----------------------------------------------------------Product--------------------------------------------------------------------------------------------#
main_menu = int(input(
    "Please type'1'to continue the product menu options, type'2' to continue the order menu options, type '0' to exit the app."))

if main_menu == 0:
    exit_func()

elif main_menu == 1:
    customer_product_order = int(input(
        "Please type '1' to see the product menu, type '2' to ask for new product, type '3' to update the product list, type '4' to delete a product, type '0' to go back to the main menu."))

    if customer_product_order == 0:
        call_main_menu()

    elif customer_product_order == 1:
        print_product_list()

    elif customer_product_order == 2:
        create_new_product()

    elif customer_product_order == 3:
        update_existing_product()

    elif customer_product_order == 4:
        delete_product()

    else:
        print("Your information is wrong.")

# ----------------------------------------------------------Order--------------------------------------------------------------------------------------------#
elif main_menu == 2:
    customer_detail_order = int(input(
        "Please type '1' to see the order menu, type '2' to make a new order, type '3' to update existing order status, type '4' to update existing order, type'5' to delete an order, type '0' to go back to the main menu."))

    if customer_detail_order == 0:
        call_main_menu()

    elif customer_detail_order == 1:
        print_order()

    elif customer_detail_order == 2:
        create_order()

    elif customer_detail_order == 3:
        update_existing_status()

    elif customer_detail_order == 4:
        update_existing_order()

    elif customer_detail_order == 5:
        delete_order()

# ----------------------------------------------------------Courier--------------------------------------------------------------------------------------------#
elif main_menu == 3:
    courier_detail = int(input(
        "Please type '1' to see the courier list, type '2' to create a new courier, type '3' to update existing courier, type '4' to delete a courier, type '0' to go back to the main menu."))

    if courier_detail == 0:
        call_main_menu()

    elif courier_detail == 1:
        print_courier()

    elif courier_detail == 2:
        create_courier()

    elif courier_detail == 3:
        update_courier()

    elif courier_detail == 4:
        delete_courier()

# --------------------------------------------------------------------Writing data to courier_record.txt---------------------------------------------------------------#
lines = courier_list
with open('courier_record.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# --------------------------------------------------------------------Writing data to product_record.txt---------------------------------------------------------------#

product_lines = product_menu_list
with open('product_record.txt', 'w') as f:
    for key, value in product_lines.items():
        f.write(f'{key}\n')
        for v in value:
            f.write(f'    {v}\n')
        f.write('\n')