import os
import json
import random

DIRECTORY_PATH = './data'
ORIGINAL_FILE_PATH = f'{DIRECTORY_PATH}/original_file.txt'
LATEST_FILE_PATH = f'{DIRECTORY_PATH}/latest_file_path.txt'
items_list = list()

if os.path.exists(DIRECTORY_PATH) == False:
    os.makedirs(DIRECTORY_PATH, exist_ok=True)
    print(f'Folder "data" is created in the "{DIRECTORY_PATH}"')

def show_list(location):
    items_list = List_Record(location)
    if not items_list:
        print('There is not item!')
        return
    if location == ORIGINAL_FILE_PATH:
        print('List the Original List Items:')
    else:
        print('List the Latest List Items:')

    for i in range(len(items_list)):
        print(f'{i}. {items_list[i]}')

def remove_item(location, item_ID):
    items_list = List_Record(location)
    if item_ID > (len(items_list)-1):
        print('Please input the range of items ID')
        return
    else:
        if location == ORIGINAL_FILE_PATH:
            user_input = input(f'Do you remove item {items_list[item_ID]} from Original List(Y/N) ').strip().upper()
        elif location == LATEST_FILE_PATH:
            user_input = input(f'Do you remove item {items_list[item_ID]} from Latest List(Y/N) ').strip().upper()

        if user_input == 'Y':
            removed_item = items_list.pop(item_ID)
            write_file(location, items_list)
            print(f'The item {removed_item} is removed')
        elif user_input == 'N':
            print(f'Cancel to reomve item {items_list[item_ID]}')
        else:
            print('Input Error')
            return

def List_Record(location):
    with open(location, 'r', encoding='utf-8') as file:
        all_items = json.load(file)
    return all_items

def item_choose(items_list):
    choose_item = items_list[random.randrange(0,len(items_list))]
    return choose_item

def write_file(location, items_list):
    with open(location, 'w', encoding='utf-8') as file:
        json.dump(items_list, file, ensure_ascii=False, indent=2)
    print(f"{os.path.basename(location)} is written!")

def create_original_list():
    items_list = []
    num_input = int(input('How many items do you want to input? ').strip())

    for i in range(num_input):
        item_input = input(f'What is item {i} name? ').strip()
        if item_input in items_list:
            print(f'{item_input} was in items list')
            continue
        else:
            items_list.append(item_input)

    if not items_list:
        print('Creating a original list is fail')
    else:
        write_file(ORIGINAL_FILE_PATH, items_list)
        write_file(LATEST_FILE_PATH, items_list)

while True:
    print('\n')
    print('---------------------------------------------------------------')
    print('Welcome to Random Choose')
    print('---------------------------------------------------------------')
    print('1. Show Original List    2. Show Latest List')
    print('3. Create Original List  4. Add a New Item to Latest List')
    print('5. Show Random Result    6. Reset Latest List')
    print('7. Remove Item           8. Exit')
    print('---------------------------------------------------------------')

    func_input = input('Which one do you choose? ').strip()

    print('\n')

    match  func_input:
        case '1':
            if os.path.exists(ORIGINAL_FILE_PATH):
                show_list(ORIGINAL_FILE_PATH)
            else:
                print('Please create a original list first!')

        case '2':
            if os.path.exists(LATEST_FILE_PATH):
                show_list(LATEST_FILE_PATH)
            else:
                print('Please create a original list first!')

        case '3':
            if os.path.exists(ORIGINAL_FILE_PATH):

                print('The original is exist')
                print('The old original & latest list will be replace')

                user_input = input('Do you want to create a New original list(Y/N) ').strip().upper()

                if user_input == "Y":
                    create_original_list()
                else:
                    print('Exit')

            else:
                create_original_list()

        case '4':
            if os.path.exists(LATEST_FILE_PATH):
                items_list = List_Record(LATEST_FILE_PATH)
                item_input = input('What is item name? ').strip()

                if item_input in items_list:
                    print(f'{item_input} was in items list')
                else:
                    items_list.append(item_input)
                    write_file(LATEST_FILE_PATH, items_list)

                    user_input = input(f'Do you want to add {item_input} to original list(Y/N) ').strip().upper()
                    if user_input == "Y":
                        items_list = List_Record(ORIGINAL_FILE_PATH)

                        if item_input in items_list:
                            print(f'{item_input} was in items list')
                        else:
                            items_list.append(item_input)
                            write_file(ORIGINAL_FILE_PATH, items_list)

                    elif user_input == "N":
                        print('Exit')

                    else:
                        print('Input Error')
            else:
                print('Please create a original list first!')


        case '5':
            if os.path.exists(ORIGINAL_FILE_PATH):
                user_input = input('Do you want to use original list(Y/N) ').strip().upper()

            if os.path.exists(LATEST_FILE_PATH) and user_input == 'N':
                items_list = List_Record(LATEST_FILE_PATH)

                choosed_item = item_choose(items_list)
                print(f'The random item is {choosed_item}')

                user_input = input(f'Do you want to remove {choosed_item} from latest list(Y/N) ').strip().upper()
                if user_input == 'Y':
                    items_list.remove(choosed_item)
                    write_file(LATEST_FILE_PATH, items_list)

            elif os.path.exists(ORIGINAL_FILE_PATH):
                items_list = List_Record(ORIGINAL_FILE_PATH)

                print(f'The random item is {item_choose(items_list)}')

            else:
                print('There is not exist original/latest list')
                user_input = input('Do you want to create a original list(Y/N) ').strip().upper()

                if user_input == "Y":
                    create_original_list()

                elif user_input == "N":
                    print('Exit')

                else:
                    print('Input Error')

        case '6':
            if os.path.exists(ORIGINAL_FILE_PATH):
                items_list = List_Record(ORIGINAL_FILE_PATH)
                write_file(LATEST_FILE_PATH, items_list)
            else:
                print('Please create a original list first!')

        case '7':
            if (os.path.exists(ORIGINAL_FILE_PATH) == True) or (os.path.exists(LATEST_FILE_PATH) == True):
                user_input = input('Which original/latest list do you want to remove the item from(O/L) ').strip().upper()

                if user_input == 'O':
                    if os.path.exists(ORIGINAL_FILE_PATH):
                        show_list(ORIGINAL_FILE_PATH)
                        try:
                            user_input = int(input("Which item do you want to remove? Please input item ID: "))
                            remove_item(ORIGINAL_FILE_PATH, user_input)
                        except ValueError:
                            print('Please input the number of the item ID')

                    else:
                        print("There is not exist original list")

                elif user_input == 'L':
                    if os.path.exists(LATEST_FILE_PATH):
                        show_list(LATEST_FILE_PATH)
                        try:
                            user_input = int(input("Which item do you want to remove? Please input item ID: ").strip())
                            remove_item(LATEST_FILE_PATH, user_input)
                        except ValueError:
                            print('Please input the number of the item ID')
                    else:
                        print("There is not exist latest list")

                else:
                    print('Input Error')

            else:
                print('Please create a original list first!')

        case '8' | 'exit':
            print('Bye')
            break
        
        case _:
            print('Input Error')
            break