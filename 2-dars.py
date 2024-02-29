# 1 - misol ------------------------------------------------------------------------------------

# import sqlite3
#
# connection = sqlite3.connect("user.db")
# cursor = connection.cursor()
#
# cursor.executescript('''
#     drop table if exists users;
#     create table if not exists users(
#         id integer primary key autoincrement,
#         name text,
#         lastname text,
#         age integer,
#         phone text,
#         email_address text
#     );
# ''')
# users_data = [("Toxir", "Toxirov", 23, "+998911234567", "toxir123@gamail.com"),
#               ("Sobir", "Toxirov", 24, "+998911234561", "sobir123@gamail.com"),
#               ("Ali", "Sobirov", 25, "+998911234564", "ali123@gamail.com"),
#               ("Bunyod", "Aliyev", 26, "+998911234568", "bunyod123@gamail.com"),
#               ("Muslim", "Sobirov", 27, "+998911234569", "muslim123@gamail.com")
#               ]
#
# cursor.executemany("insert into users (name, lastname, age, phone, email_address) values (?,?,?,?,?);", users_data)
#
# cursor.executescript("update users set age = 26 where id = 2")
# cursor.executescript("update users set age = 26 where name = 'Toxir'")
#
# cursor.execute("delete from users where name = 'Toxir'")
#
# cursor.execute("select * from users order by name")
# users_data = cursor.fetchall()
# print("ismlari tartibi bo'yicha ekranga chiqarildi")
# for user in users_data:
#     print(f"ismi: {user[1]}\n"
#           f"familyasi: {user[2]}\n"
#           f"yoshi: {user[3]}\n"
#           f"nomeri: {user[4]}\n"
#           f"email_addresi: {user[5]}\n")
#
# cursor.execute("select * from users order by name desc")
# users_data = cursor.fetchall()
# print(f"ismlari teskari tartib bo'yicha ekranga chiqarildi")
# for user in users_data:
#     print(f"ismi: {user[1]}\n"
#           f"familyasi: {user[2]}\n"
#           f"yoshi: {user[3]}\n"
#           f"nomeri: {user[4]}\n"
#           f"email_addresi: {user[5]}\n")
#
# cursor.execute("select * from users where age > 18 order by age")
# users_data = cursor.fetchall()
# print(f"yoshlari 18 dan kattalari ekaranga chiqarildi")
# for user in users_data:
#     print(f"ismi: {user[1]}\n"
#           f"familyasi: {user[2]}\n"
#           f"yoshi: {user[3]}\n"
#           f"nomeri: {user[4]}\n"
#           f"email_addresi: {user[5]}\n")
#
# cursor.execute("select * from users where age < 18 order by age")
# users_data = cursor.fetchall()
# print(f"18 - yoshdan kichkinalari ekranga chiqarildi")
# for user in users_data:
#     print(f"ismi: {user[1]}\n"
#           f"familyasi: {user[2]}\n"
#           f"yoshi: {user[3]}\n"
#           f"nomeri: {user[4]}\n"
#           f"email_addresi: {user[5]}\n")
#
# print("userlar soni: ")
# cursor.execute("select count(*) from users")
# user_data = cursor.fetchone()
# print(user_data)
#
#
# connection.commit()
# connection.close()


# 2 - misol ------------------------------------------------------------------------------------

# import sqlite3
#
# connection = sqlite3.connect("maxsulotlar.db")
# cursor = connection.cursor()
# 
# cursor.executescript('''
#     drop table if exists categories;
#     create table if not exists categories(
#         id integer primary key autoincrement,
#         name text
#     );
# ''')
#
# cursor.executescript('''
#     drop table if exists products;
#     create table if not exists products(
#         id integer primary key autoincrement,
#         name text,
#         category_id integer references categories(id),
#         price integer
#     );
# ''')
#
# category_data = [("meva",),
#                  ("sabzavot",),
#                  ("elektro texnika",),
#                  ("telefon",)]
#
# cursor.executemany("insert into categories (name) values (?)", category_data)
#
# products_data = [("olma", 1, 100),
#                  ("bexi", 1, 200),
#                  ("kartosha", 2, 300),
#                  ("piyoz", 2, 400),
#                  ("televizor", 3, 500),
#                  ("fen", 3, 350),
#                  ("iphone 14", 4, 1000),
#                  ("samsung s24", 4, 800)]
#
# cursor.executemany("insert into products (name, category_id, price) values (?, ?, ?)", products_data)
#
# print("productning maxsulotlar nonini chiqarish! ")
# cursor.execute("select count(*) from products")
# product = cursor.fetchone()
# print(product)
#
# print("categoryaning nechtaligini chiqarish! ")
# cursor.execute("select count (*) from categories")
# category = cursor.fetchone()
# print(category)
#
# print("category bilan productning boglangan jadvalini chiqarish ")
# cursor.execute("select products.name, products.price, categories.name "
#                "from products join categories "
#                "on products.category_id = categories.id")
# products_category = cursor.fetchall()
# for i in products_category:
#     print(f"nomi: {i[0]}\n"
#           f"narxi: {i[1]}\n"
#           f"categoriyasi: {i[2]}\n")
#
# print("eng qimmat productni chiqarish! ")
# cursor.execute("select * from products order by price desc limit 1")
# product = cursor.fetchone()
# print(product, "\n")
#
# print("eng arzon productni chiqarish! ")
# cursor.execute("select * from products order by price limit 1")
# product = cursor.fetchone()
# print(product, "\n")
#
# print("barcha productlarning umumiy narxi! ")
# cursor.execute("select sum(price) from products")
# product = cursor.fetchone()
# print(product, "\n")
#
# print("3 ta eng qimmat productni chiqarish! ")
# cursor.execute("select * from products order by price desc limit 3")
# product = cursor.fetchall()
# for i in product:
#     print(i)
# print()
#
# print("3 ta eng arzon productni chiqarish! ")
# cursor.execute("select * from products order by price limit 3")
# product = cursor.fetchall()
# for i in product:
#     print(i)
# print()
#
# print("Barcah productalarni tartiblab chiqarish! ")
# cursor.execute("select products.name, products.category_id, categories.name "
#                "from products join categories "
#                "on products.category_id = categories.id "
#                "order by products.name")
#
# product_category = cursor.fetchall()
# for i in products_category:
#     print(f"nomi: {i[0]}\n"
#           f"narxi: {i[1]}\n"
#           f"categoriyasi: {i[2]}\n")
#
#
# connection.commit()
# connection.close()
