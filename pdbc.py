import pymysql

# MySQL root credentials
host = "127.0.0.1"
user = "root"       # or another MySQL user with CREATE DATABASE privilege
password = "RootPass#2025"

# Database name you want to create
db_name = "shopkartdb"

# Connect to MySQL server (without specifying a DB)
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print(f"Database '{db_name}' created successfully (or already exists).")
finally:
    connection.close()
