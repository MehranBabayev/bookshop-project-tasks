import sys
from datetime import datetime
from os.path import exists
if not exists ("book_list.txt"):
    file=open("book_list.txt", "x")
command =sys.argv

class Book:
    
    def set_id(self):
        with open('book_list.txt', 'r+') as f:
            obj = f.readlines()
            last_id = 1
            if obj:
                last_id = int(obj[-5].split(':')[1]) + 1
            ele = f'ID : {last_id}'
            f.write(f"{ele}\n")
        return True  

    def add_book(self):
        title = input('Please enter book name: \n ')
        writer = input('Please enter writer name: \n ')
        with open('book_list.txt', 'a+') as f:
            ele = f'Book name : {title}\nWriter name : {writer}'
            f.write(f"{ele}\n")
            print("\nAdded succesfully!")
        return True
    
    def set_date(self):
        with open('book_list.txt', 'a+') as f:
            obj = f.readlines()
            ele = f'Added in : {datetime.today().strftime("%d %B %Y")}'
            f.write(f"{ele}\n{'*' * 50}\n")
        
        
    def show_book(self):
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
    def show_all(self):
        with open("book_list.txt", "r") as f:
            obj=f.readlines()
            for i in range(0, len(obj), 5):
                search = obj[-5].split(":")[1].strip()
                count=0
                if count<int(search):
                    count=search
            print(f"There are {count} books")
            print(*obj)
            
    def remove_book(self):
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
                
book=Book()                
if len(command) == 2 and command[1] == 'add':
    book.set_id()
    book.add_book()
    book.set_date()
elif len(command) == 3 and command[1] == 'show' and command[2] == 'all':
    book.show_all()
elif len(command) == 3 and command[1] == 'show' and command[2] == 'book':
    book. show_book()
elif len(command) == 2 and command[1] == 'remove':
    book.remove_book()
else:
    print('Please, enter right input')
