import sys
from datetime import datetime
from os.path import exists
if not exists ("book_list.txt"):
    file=open("book_list.txt", "x")
command =sys.argv
def add_book():
    title = input('Please enter book name: ')
    writer = input('Please enter writer name: ')
    with open('book_list.txt', 'r+') as f:
        obj = f.readlines()
        last_id = 1
        if obj:
            last_id = int(obj[-5].split(':')[1]) + 1
        ele = f'ID : {last_id}\nBook name : {title}\nWriter name : {writer}\nAdded in : {datetime.today().strftime("%d %B %Y")}'
        f.write(f"{ele}\n{'*' * 50}\n")
        print("\nAdded succesfully!")

    return True
def show_book():
    id = input('Please enter ID: ' )
    f = open('book_list.txt', 'r+')
    obj = f.readlines()
    for i in range(0, len(obj), 5):
        search = obj[i].split(':')[1].strip()
        if id == search:
            index = i
            range_list = [index, index + 1, index + 2, index + 3, index+4]
            for i in range(len(obj)):
                    if i in range_list:
                        print(obj[i])
            break
def show_all():
    with open("book_list.txt", "r") as f:
        obj=f.readlines()
        for i in range(0, len(obj), 5):
            search = obj[-5].split(":")[1].strip()
            count=0
            if count<int(search):
                count=search
        print(f"There are {count} books")
        print(*obj)
        
def remove_book():
    id = input('Please enter ID: ' )
    with open('book_list.txt', 'r+') as file:
        obj = file.readlines()
        file.seek(0)
        for line in range(0, len(obj), 5):
            remove_ele = obj[line].split(':')[1].strip()
            if id == remove_ele:
                index = line
                range_list = [index, index + 1, index + 2, index + 3, index + 4]
                file.truncate()
                for i in range(len(obj)):
                    if i not in range_list:
                        file.write(obj[i])
                print('\nSuccesfully deleted!\n')
                break
        else:
            print('\nID does not exist!\n')
if "add" in command:
    add_book()
elif"show" and "book" in command:
    show_book()
elif"show" and "all" in command:
    show_all()
elif "remove" and "book" in command:
    remove_book()
