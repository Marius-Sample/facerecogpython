from supabase import create_client
import psycopg2 as pg

supabase = create_client(API_URL, API_KEY)

# database that handles local database
class Database():
    API_KEY= "https://hphnqflbwqmfdvsfqkqi.supabase.co",
    API_URL= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwaG5xZmxid3FtZmR2c2Zxa3FpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE1MjkwNjcsImV4cCI6MjAyNzEwNTA2N30.TA6JQ3L8ML7yv4f2Tst4dJ8MsokYmcc5JLKU2-iumiI"
    
    host="localhost"
    dbname="postgres"
    user="postgres"
    password="Classroom_00"
    
    cur=""
    
    def __init__(self):
        conn= pg.connect(self.host, self.dbname, self.user, self.password)
        self.cur= conn.cursor()
        
        
    
    def sanitizeInput(self, query):
        pass
    
    # def createTable(self, query):
    #     self.cur.execute("""CREATE TABLE IF NOT EXISTS person(
    #         id INT PRIMARY KEY,
    #         name VARCHAR(255),
    #         age INT,
    #         gender CHAR
    #     )
    #     """)


    #     cur.execute(""" INSERT INTO person (name, age, gender) VALUES('Marius', 20, 'M')""")

    #     conn.commit()
    #     cur.close()
    #     conn.close()
    # def insert