import psycopg2
from pprint import pprint


def create_db(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
        client_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(200) UNIQUE 
        );         
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,    
        client_id INTEGER NOT NULL REFERENCES clients(client_id),
        phone VARCHAR(11) UNIQUE
        );         
    """)
    

def add_client(cur, first_name, last_name, email):
    cur.execute("""
    INSERT INTO clients(first_name, last_name, email)  
    VALUES (%s, %s, %s);           
    """, (first_name, last_name, email))
    

def add_phone(cur, client_id, phone):
    cur.execute("""
    INSERT INTO phones(client_id, phone)  
    VALUES (%s, %s);           
    """, (client_id, phone))
    

def change_client(cur):
    print("Для изменения информации o клиенте введите соответствующую цифру: \n "
        "1 - изменить имя; 2 - изменить фамилию; 3 - изменить e-mail; 4 - изменить номер телефона")
    while True:
        num = int(input())
        if num == 1:
            c1_id = input("Введите id клиента имя которого хотите изменить: ")
            new_name = input("Введите имя для изменения: ")
            cur.execute("""
            UPDATE clients SET first_name=%s WHERE client_id=%s;
            """, (new_name, c1_id))
            break
        elif num == 2:
            c2_id = input("Введите id клиента фамилию которого хотите изменить: ")
            new_surname = input("Введите фамилию для изменения: ")
            cur.execute("""
            UPDATE clients SET last_name=%s WHERE client_id=%s;
            """, (new_surname, c2_id))
            break
        elif num == 3:
            c3_id = input("Введите id клиента e-mail которого хотите изменить: ")
            new_email = input("Введите e-mail для изменения: ")
            cur.execute("""
            UPDATE clients SET email=%s WHERE client_id=%s;
            """, (new_email, c3_id))
            break
        elif num == 4:
            changing_phone = input("Введите номер телефона который хотите изменить: ")
            new_phone = input("Введите новый номер телефона: ")
            cur.execute("""
            UPDATE phones SET phone=%s WHERE phone=%s;
            """, (new_phone, changing_phone))
            break
        else:
            print("Неверная команда, повторите ввод")
            
            

def delete_phone(cur, client_id, phone):
    cur.execute("""
    DELETE FROM phones WHERE client_id=%s AND phone=%s;
    """, (client_id, phone))
   

def delete_client(cur, client_id):
    cur.execute("""
        DELETE FROM phones WHERE client_id = %s;
        """, (client_id, ))
    cur.execute("""
        DELETE FROM clients WHERE client_id = %s;
       """, (client_id,))
   

def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    if first_name is not None:
        cur.execute("""
           SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone FROM clients c
           LEFT JOIN phones p USING(client_id)  
           WHERE c.first_name LIKE %s      
        """, (first_name,))
        pprint(cur.fetchall())
    elif last_name is not None:
        cur.execute("""
           SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone FROM clients c
           LEFT JOIN phones p USING(client_id)  
           WHERE c.last_name LIKE %s       
        """, (last_name,))
        pprint(cur.fetchall())
    elif email is not None:
        cur.execute("""
           SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone FROM clients c
           LEFT JOIN phones p USING(client_id)  
           WHERE c.email LIKE %s       
        """, (email,))
        pprint(cur.fetchall())
    elif phone is not None:
        cur.execute("""
           SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone FROM clients c
           LEFT JOIN phones p USING(client_id)  
           WHERE p.phone LIKE %s       
        """, (phone,))
        pprint(cur.fetchall())    
        
def delete_db(cur):
    cur.execute("""
        DROP TABLE clients, phones CASCADE;
        """)
        
        
if __name__ == '__main__':  
    with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
         with conn.cursor() as cur:
             delete_db(cur)
             create_db(cur)
             add_client(cur, "Виктор", "Дмитриев", "123@mail.ru")
             add_client(cur, "Светлана", "Петрова", "456@mail.ru")
             add_client(cur, "Евгений", "Смирнов", "321@mail.ru")
             add_client(cur, "Петр", "Сальников", "853@mail.ru")
             add_phone(cur, 1, "9761234056")    
             add_phone(cur, 2, "9811426456") 
             add_phone(cur, 3, "9736123456") 
             add_phone(cur, 4, "9761223456")   
             find_client(cur, "Виктор")
             find_client(cur, None, "Смирнов")
             find_client(cur, None, None, "853@mail.ru")
             find_client(cur, None, None, None, "9736123456")
             change_client(cur)
             delete_phone(cur, 1, "9761234056")
             delete_client(cur, 2)
             

    conn.close()