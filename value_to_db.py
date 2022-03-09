import sqlite3

conn = sqlite3.connect('movie.db')
conn.execute(''' CREATE TABLE MOVIE
     (NAME TEXT NOT NULL,
     ACTOR TEXT NOT NULL,
     ACTRESS TEXT NOT NUll,
     YEAR INT NOT NULL,
     DIRECTOR TEXT NOT NULL);''')
conn.execute("INSERT INTO MOVIE(NAME,ACTOR,ACTRESS,YEAR,DIRECTOR) VALUES('SpiderMan:No way home','Tom Holland','Zendaya',2022,'Jon Watts')");
conn.execute("INSERT INTO MOVIE(NAME,ACTOR,ACTRESS,YEAR,DIRECTOR) VALUES('Tenet','John David Washington','Elizabeth Debicki',2020,'Christopher Nolan')");
conn.execute("INSERT INTO MOVIE(NAME,ACTOR,ACTRESS,YEAR,DIRECTOR) VALUES('Fantastic Beasts and Where to Find Them','Eddie Redmayne','Katherine Waterston',2016,'David Yates')");
conn.commit()
print("Values added to SQLite database")
conn.close()
