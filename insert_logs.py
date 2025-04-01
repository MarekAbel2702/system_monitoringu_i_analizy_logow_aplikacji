from parse_logs import parse_log_line
from connect_db import get_connection

def insert_logs_from_file(file_path):
    conn = get_connection()
    cursor = conn.cursor()

    inserted_count = 0

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                log_time, level, message = parsed
                cursor.execute("""
                    INSERT INTO Logs (log_time, level, message)
                    VALUES (?, ?, ?)
                """, log_time, level, message)
                inserted_count += 1

    conn.commit()
    conn.close()
    print(f"✅ Wstawiono {inserted_count} logów do bazy danych.")

if __name__ == "__main__":
    insert_logs_from_file("data/sample_logs.log")