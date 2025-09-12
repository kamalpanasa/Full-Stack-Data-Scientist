def add_item(menu, item):
    menu.append(item)
    return menu
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        return f"{item} not found in the menu"
    return menu
def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"
    

list1 = input("Enter the initial menu items separated by commas: ").split(",")

add_item_name = input("Enter the item to add: ")
remove_item_name = input("Enter the item to remove: ")
check_item_name = input("Enter the item to check availability: ")
updated_menu = add_item(list1, add_item_name)


print("Updated menu ", updated_menu)
updated_menu = remove_item(updated_menu, remove_item_name)
print("Updated menu ", updated_menu)
print(check_item(updated_menu, check_item_name))