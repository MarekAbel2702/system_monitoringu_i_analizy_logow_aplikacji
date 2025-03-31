from connect_db import get_connection

try:
    conn = get_connection()
    print("✅ Połączenie z bazą danych działa!")
    conn.close()
except Exception as ex:
    print("❌ Błąd połączenia:", ex)