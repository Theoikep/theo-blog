import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'tradeNews',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute("""CREATE TABLE IF NOT EXISTS admins(
    ID INT AUTO_INCREMENT,
    Title VARCHAR(250) NOT NULL,
    Descriptions VARCHAR(2000000000) NOT NULL,
    IMG VARCHAR(300) NOT NULL,
    PRIMARY KEY(ID)
)""")
