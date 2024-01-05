import sqlite3
class Databese:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        sql="""
            CREATE  TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT ,
            position TEXT ,
            gender TEXT ,
            age TEXT ,
            email TEXT ,
            phone TEXT ,
            address TEXT 
            );
            """
        self.cursor.execute(sql)
        self.conn.commit()
    def insert(self,name,Position,gender,age,email,phone,address):
        self.cursor.execute("insert into employees values(NULL,?,?,?,?,?,?,?)",
                            (name,Position,gender,age,email,phone,address)
                           )
        self.conn.commit()
    def fetch(self):
        self.cursor.execute("select * from employees")
        row = self.cursor.fetchall()
        return row
    def delete(self,id):
        self.cursor.execute("delete from employees where id=?",(int(id),))
        self.conn.commit()
    def update(self,id,name,Position,gender,age,email,phone,address):
        self.cursor.execute("update employees set name=?,position=?,gender=?,age=?,email=?,phone=?,address=? where id=?",
                            (name,Position,gender,age,email,phone,address,id)
                           )
        self.conn.commit()
        