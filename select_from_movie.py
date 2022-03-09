import sqlite3

conn = sqlite3.connect('movie.db')

cursor = conn.execute("SELECT * from MOVIE")
for row in cursor:
     print("Movie :",row[0])
     print("Actor :",row[1])
     print("Actress :",row[2])
     print("Year :",row[3])
     print("Director :",row[4])
     print("")

print("Table printed successfully.")
conn.close()
