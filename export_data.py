import pandas as pd
from connect_db import get_connection

def export_logs():
    conn = get_connection()

    df = pd.read_sql("SELECT * FROM Logs", conn)

    df.to_csv("export/logs.csv", index=False)
    print("✅ Zapisano do export/logs.csv")

    df.to_json("export/logs.json", orient="records", indent=4)
    print("✅ Zapisano do export/logs.json")

    df.to_xml("export/logs.xml", index=False)
    print("✅ Zapisano do export/logs.xml")

    df.to_html("export/logs.html", index=False)
    print("✅ Zapisano do export/logs.html")

    conn.close()

if __name__ == "__main__":
    export_logs()