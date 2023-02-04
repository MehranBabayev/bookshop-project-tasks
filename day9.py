import pymysql.cursors
import datetime
import sys

from os.path import exists
command =sys.argv


connection = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "12345",
                             db = "project",
                             charset = "utf8mb4",
                             cursorclass = pymysql.cursors.DictCursor)
    
    

def create_table():
    with connection.cursor() as cursor:
        sql = """
        create table if not exists Book_info(
        Book_id int not null auto_increment primary key,
        Book_name varchar(255) not null,
        Writer varchar(255) not null,
        Added_in date not null,
        Exist boolean  not null, 
        Price integer not null
        ) 
        """
        cursor.execute(sql)
    connection.commit()

   
    
    
def create_book():
    with connection.cursor() as cursor:
        Book_name = input("Enter book name:\n")
        Writer = input("\nEnter writer name:\n")
        Added_in = datetime.datetime.today()
        Price = int(input("\nEnter price of book:\n"))
        Exist = input("\nEnter existence:\n")
        sql = """
        insert into Book_info(Book_name, Writer, Added_in, Price, Exist) values(%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (Book_name, Writer, Added_in, Price,Exist))
    connection.commit()


def show_all ():
    with connection.cursor() as cursor:
        sql = ''' select * from Book_info 
        '''
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)    


def show_all():
    with connection.cursor() as cursor:
        sql = ''' select * from Book_info 
        '''
        cursor.execute(sql)
        result = cursor.fetchall()
    for i in result:
        print(i) 


def show_book ():
    with connection.cursor() as cursor:
        id = int(input("Enter book_id:\n"))
        sql = f''' select * from Book_info where Book_id =  {id}
        '''
        cursor.execute(sql)
        result = cursor.fetchone() 
        print(result)

def change_status ():
    with connection.cursor() as cursor:
        id = int(input("Enter book_id:\n"))
        sql = f''' update Book_info set Exist = Case 
        when exist = true then false
        when exist = false then true
        End
        where Book_id =  {id}
        
        '''
        cursor.execute(sql)
    connection.commit()
        
def change_price ():
    with connection.cursor() as cursor:
        id = int(input("Enter book_id:\n"))
        new_price = int(input("Enter new_price:\n"))
        sql = f''' update Book_info set Price= {new_price}
        where Book_id =  {id}
        
        '''
        cursor.execute(sql)
    connection.commit()
        

def remove_book ():
    with connection.cursor() as cursor:
        id = int(input("Enter book_id:\n"))
        
        sql = f''' delete from Book_info 
        where Book_id =  {id}
        
        '''
        cursor.execute(sql)
    connection.commit()
    
    
def search_book ():
    with connection.cursor() as cursor:
        search_word = input("Enter search_word:\n")
        
        sql = f''' select * from Book_info 
        where Book_name  like "%{search_word}%" and writer like "%{search_word}%"
        
        '''
        cursor.execute(sql)
        result= cursor.fetchall()
        print(result)

    
if len(command) == 3 and command[1] == 'add' and command[2] == 'table':
    create_table()  
elif len(command) == 3 and command[1] == 'add' and command[2] == 'book':
    create_book() 
elif len(command) == 3 and command[1] == 'show' and command [2] == 'all':
    show_all()            
elif len(command) == 3 and command[1] == 'show' and command [2] == 'book':
    show_book()
elif len(command) == 3 and command[1] == 'change' and command [2] == 'status':
    change_status()
elif len(command) == 3 and command[1] == 'change' and command [2] == 'price':
    change_price()
elif len(command) == 2 and command[1] == 'remove':
    remove_book()
elif len(command) == 2 and command[1] == 'search':
    search_book()