import mysql.connector

mydb = mysql.connector.connect(
     host='127.0.0.1',
    user = 'root',
    password = 'leviAthan99!',
    database = 'mydatabase'
)
mycursor = mydb.cursor()

#mycursor.execute('CREATE DATABASE mydatabase')

#mycursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')

#mycursor.execute('SHOW TABLES')


#for x in mycursor:
#    print(x)

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") TABLO ZATEN VARSA ALER_TABLE


# sql = "INSERT INTO customers (name, address) VALUES(%s,%s)"
# val = ('John', 'Highway 21')
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, 'record inserted')
#Bir tabloya birden çok satır eklemek için executemany() yöntemini kullanın.
#Executemany() yönteminin ikinci parametresi, eklemek istediğiniz verileri içeren bir demet listesidir:
# sql = "INSERT INTO customers (name, address) VALUES(%s,%s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()


# mycursor.execute('SELECT * FROM customers')

# myresult = mycursor.fetchall()
# for x in myresult:
    # print(x)
#Not: Son yürütülen ifadeden tüm satırları getiren fetchall() yöntemini kullanıyoruz.

mycursor.execute('SELECT name,address FROM customers')

myresult = mycursor.fetchall()
for x in myresult:
    print(x)