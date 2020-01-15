import psycopg2
from psycopg2 import sql
from app import app,conn


cursor = conn.cursor()

try:

    cursor.execute(

        "CREATE TABLE if not exists customer (id_customer serial primary key, login varchar(15) NOT null, password varchar(100) NOT NULL, email TEXT NOT NULL);")

    conn.commit()

    cursor.execute(

        "CREATE TABLE if not exists master (id_master int primary key, login varchar(15) NOT null unique, password varchar(100) NOT NULL, description TEXT NOT NULL unique, picture TEXT NOT NULL, history TEXT NOT NULL);")

    conn.commit()

    # references person(table)
    cursor.execute(

        "CREATE TABLE if not exists category  (id_category  int primary key, description_category TEXT NOT NULL, name_category TEXT NOT NULL);")

    conn.commit()




    cursor.execute(

        "CREATE TABLE if not exists ord  (id_customer serial REFERENCES  customer, id_order serial primary key,  id_product  int  REFERENCES  product, "
        " name_of_product TEXT NOT NULL, product_description TEXT NOT NULL ,  "
        "image TEXT NOT NULL, price int NOT null,date_order date NOT NULL);")

    conn.commit()


    cursor.execute(

        "CREATE TABLE if not exists product(id_product serial  primary key,id_category int REFERENCES category, name_of_product TEXT NOT NULL,"
        " product_description TEXT NOT NULL, image TEXT NOT NULL, price INT NOT NULL, quantity_in_stock int NOT NULL);")
    conn.commit()




    cursor.execute(

        "CREATE TABLE if not exists exclusive_product(id_exclusive_product int primary key, id_master int  REFERENCES master, image_exclusive TEXT NOT NULL, id_category int unique REFERENCES category  );")

    conn.commit()

#   cursor.execute(
#
#       "CREATE TABLE if not exists goods_in_order(FOREIGN KEY id_order REFERENCES ord"
#       "id_goods_in_order int primary key, order_quantity int NOT NULL,history_list TEXT NOT NULL, "
#       " FOREIGN KEY (id_product) REFERENCES (product),"
#       " FOREIGN KEY (id_exclusive_product) REFERENCES (exclusive_product)  );")

#   conn.commit()



except Exception as e:

    print(e)