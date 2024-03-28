import psycopg2 as pg

conn= pg.connect(host="localhost", dbname="postgres", user="postgres", password="Classroom_00")

cur= conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
)
""")


cur.execute(""" INSERT INTO person (name, age, gender) VALUES('Marius', 20, 'M')""")

conn.commit()
cur.close()
conn.close()
