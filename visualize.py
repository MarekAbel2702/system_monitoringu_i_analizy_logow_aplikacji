import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from connect_db import get_connection

def visualize_logs():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Logs", conn)
    conn.close()

    sns.set(style="whitegrid")

    plt.figure(figsize=(6, 4))
    level_counts = df['level'].value_counts()
    sns.barplot(x=level_counts.index, y=level_counts.values)
    plt.title("Liczba logów wg poziomu")
    plt.xlabel("Poziom logu")
    plt.ylabel("Liczba")
    plt.tight_layout()
    plt.savefig("export/logs_by_level.png")
    plt.show()

    df['log_time'] = pd.to_datetime(df['log_time'])
    df['hour'] = df['log_time'].dt.floor('h')
    hourly_errors = df[df['level'] == "ERROR"].groupby('hour').size()

    plt.figure(figsize=(8, 4))
    hourly_errors.plot(kind='line', marker='o')
    plt.title("Liczba błędów (ERROR) w czasie")
    plt.xlabel("Godzina")
    plt.ylabel("Liczba błędów")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("export/errors_over_time.png")
    plt.show()

if __name__ == "__main__":
    visualize_logs()
