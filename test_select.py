from connect_db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM Logs")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()