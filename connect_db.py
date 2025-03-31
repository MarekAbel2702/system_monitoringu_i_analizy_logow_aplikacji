import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={SQL Server};SERVER=LAPTOP-M79Q5NVL\\SQLEXPRESS;DATABASE=LogAnalyzer;Trusted_Connection=yes;"
    )
    return conn